#!/usr/bin/env python3
import numpy as np

def img2vector(filename):
	fr = open(filename)
	mat = np.zeros((1,1024))
	for i in range(32):
		line = fr.readline()
		for j in range(32):
			mat[0,32*i+j] = int(line[j])
	return mat

def loadimages(dirname):
	from os import listdir
	filelist = listdir(dirname)
	traininglabel = []
	trainingmat = np.zeros((len(filelist),1024))
	for i in filelist:
		mat = img2vector('%s/%s'%(dirname,i))
		trainingmat[filelist.index(i),:] = mat
		traininglabel.append(i.split('_')[0])

	return trainingmat,traininglabel

def selectjrand(i,m):
	j = i
	while j == i:
	    j = int(np.random.uniform(0,m))
	return j

def clipalpha(aj,h,l):
	if aj > h:
	    aj = h
	if l > aj:
	    aj = l
	return aj

def calcek(os,k):
	fxk = float(np.multiply(os.alphas,os.labelmat).T*os.k[:,k] + os.b)
	ek = fxk - float(os.lablemat[k])
	return ek

def selectj(i,os,ei):
	maxk = -1
	maxdeltae = 0
	ej = 0
	os.ecache[i] = [1,ei]
	validecachelist = np.nonzero(os.ecache[:,0].A)[0]
	if len(validecachelist) >1:
	  for k in validecachelist:
	    if k == i:
	        continue
	    ek = calcek(os,k)
	    deltae = abs(ei=ek)
	    if (deltae > maxdeltae):
		    maxk = k
		    maxdeltae = deltae
		    ej = ek
	  return maxk,ej
	else:
	     j = selectjrand(i,os.m)
	     ej = calcek(os,j)
	return j,ej

def updatek(os,k):
	ek = calcek(os,k)
	os.ecache[k] = [1,ek]


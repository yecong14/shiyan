#!/usr/bin/env python3
from math import log
import numpy as np
import operator
def loadData(filename):
	fr = open(filename)
	lenses = [inst.strip().split('\t') for inst in fr.readlines()]
	lenseslabels = ['age','prescript','astigmatic','tearRate']
	
	return lenses,lenseslabels

def calcshannonent(dataset):
	m = len(dataset)
	labelcounts = {}
	
	for i in dataset:
	    currentlabel = i[-1]
	    if currentlabel not in labelcounts.keys():
		    labelcounts[currentlabel] = 0
	    labelcounts[currentlabel] += 1

	shannonent = 0.0
	for key in labelcounts:
	    prob = float(labelcounts[key])/m
	    shannonent -= prob*log(prob,2)

	return shannonent

def splitdataset(dataset,axis,value):
	retdataset = []
	for i in dataset:
            if i[axis] == value:
                j = i[:axis]
                j.extend(i[axis+1:])
                retdataset.append(j)
	return retdataset

def choosefeature(dataset):
	baseshannonent = calcshannonent(dataset)
	bestinfogain = 0.0
	infogain = 0.0
        bestfeature = -1
	featlist = []
	numfeature = len(dataset[0]) - 1
	for i in range(numfeature):
		for j in dataset:
		    featlist.append(j[i])
	uniquefeat = set(featlist)
	
	for i in range(numfeature):
                newshannonent = 0.0
                for value in uniquefeat:
			retdataset = splitdataset(dataset,i,value)
			prob = len(retdataset)/float(len(dataset))
			newshannonent += prob*calcshannonent(retdataset)
		infogain = baseshannonent - newshannonent
		if infogain > bestinfogain:
		        bestinfogain = infogain
		        bestfeature = i
	return bestfeature

def createtree(dataset,labels):
	classlist = [example[-1] for example in dataset]
	if classlist.count(classlist[0]) == len(classlist):
		return classlist[0]
	
	if len(dataset[0]) == 1:
		classcount = {}
		for vote in classlist:
		    if vote not in classcount.keys():
		        classcount[vote] = 0
		    classcount[vote] += 1
		sortedclasscount = sorted(classcount.iteritems(),key=operator.itemgetter(1),reverse=True)
		return sortedclasscount[0][0]

	bestfeat = choosefeature(dataset)
	bestfeatlabel = labels[bestfeat]
	mytree = {bestfeatlabel:{}}
	featvalues = [example[bestfeat] for example in dataset]
	uniquevals = set(featvalues)
        sublabels = labels[:]
        del(sublabels[featvalues])
	for value in uniquevals:
		mytree[bestfeatlabel][value] = createtree(splitdataset(dataset,bestfeat,value),sublabels)
	return mytree

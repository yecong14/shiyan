#!/usr/bin/env python3
from numpy import *
def stumpclassify(datamatrix,dimen,threshval,threshineq):
	retarray = ones((shape(datamatrix)[0],1))
	if threshineq == 'lt':
	    retarray[datamatrix[:,dimen] <= threshval] = -1.0
	else:
	    retarray[datamatrix[:,dimen] > threshval] = -1
	return retarray

def buildstump(dataarr,classlabels,d):
	datamatrix = mat(dataarr)
	labelmat = mat(classlabels).T
	m,n = shape(datamatrix)
	numsteps = 10.0
	beststump = {}
	bestclasest = mat(zeros((m,1)))
	minerror = inf
	for i in range(n):
		rangemin = datamatrix[:,i].min()
		rangemax = datamatrix[:,i].max()
		stepsize = (rangemax-rangemin)/numsteps
		for j in range(-1,int(numsteps)+1):
			for inequal in ['lt','gt']:
	                    threshval = (rangemin+float(j)*stepsize)
			    predictedvals = stumpclassify(datamatrix,i,threshval,inequal)
			    errarr = mat(ones((m,1)))
                            errarr[predictedvals==labelmat]=0
			    weightederror = d.T*errarr
			    if weightederror < minerror:
	                        bestclasest = predictedvals.copy()
                                minerror = weightederror
                                beststump['dim'] = i
                                beststump['thresh'] = threshval
                                beststump['ineq'] = inequal
        return beststump,minerror,bestclasest


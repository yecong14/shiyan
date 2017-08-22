#!/usr/bin/env python3
import numpy as np
import operator
def classify0(inx,data,label,k):
	datasize = data.shape[0]
	daffmat = np.tile(inx,(datasize,1))-data
	sqdiffmat = daffmat**2
	distance = sqdiffmat.sum(axis=1)
	distance = distance**0.5
	sorteddistindicies = distance.argsort()
	classcount = {}
	for i in range(k):
		votelabel = label[sorteddistindicies[i]]
		classcount[votelabel] = classcount.get(votelabel,0) + 1

	sortedclasscount = sorted(classcount.iteritems(),key=lambda asd:asd[1],reverse=True)
	return sortedclasscount[0][0]

#!/usr/bin/env python3
from numpy import *
def loadsimpdata():
	datamat = matrix([[1.,2.1],
			[2.,1.1],
			[1.3,1.],
			[1.,1.],
			[2.,1.]])
	classlabels = [1.0,1.0,-1.0,-1.0,1.0]
	return datamat, classlabels


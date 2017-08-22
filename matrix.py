#!/usr/bin/env python3
import numpy as np

def file2matrix(filename):
	fr = open(filename)
	array = fr.readlines()
	numberoflines = len(array)
	matrix = np.zeros((numberoflines,3))
	label = []
	index = 0
	for i in array:
	    line = i.strip()
	    list = line.split()
	    matrix[index,:] = list[0:3]
	    label.append(int(list[-1]))
	    index += 1
	return matrix,label

def norm(matrix):
	minvals = matrix.min(0)
	maxvals = matrix.max(0)
	ranges = maxvals - minvals
	m = matrix.shape[0]
	norm = np.zeros(np.shape(matrix))
	norm = matrix - np.tile(minvals,(m,1))
	norm = norm/np.tile(ranges,(m,1))
	return norm,ranges,minvals



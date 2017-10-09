#!/usr/bin/env python3
import numpy as np
def img2vector0(filename):
	vector = np.zeros((1,1024))
	fr = open(filename)
	for i in range(32):
		linestr = fr.readline()
		for j in range(32):
			vector[0,32*i+j] = int(linestr[j])

	return vector

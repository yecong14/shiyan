from numpy import *
def loaddataset(filename):
	datamat = []
	labelmat = []
	fr = open(filename)
	lines = fr.readlines()
	for i in lines:
	    line = i.strip().split('\t')
	    word = [float(j) for j in line]
	    datamat.append(word)
	    labelmat.append(word[-1])
	return array(datamat),labelmat



#!/bin/usr/env python3
from numpy import *
def loaddataset(filename):
	datamat = []
	fr = open(filename)
	lines = fr.readlines()
	for i in lines:
		curline = i.strip().split()


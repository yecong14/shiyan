#!/usr/bin/env python3
import re

def loademailfile(filename):
		fr = open(filename)
		regex = re.compile('\W*')
		wordlist = regex.split(fr.read())
		return [i.lower() for i in wordlist if len(i)>2]

def createvocablist(doclist):
	vocabset = set([])
	for document in doclist:
		vocabset = vocabset | set(document)
	return list(vocabset)

from numpy import *
def bagofwords2vecmn(vocablist,inputset):
	returnvec = [0]*len(vocablist)
	for word in inputset:
		if word in vocablist:
		    returnvec[vocablist.index(word)] += 1
	return returnvec
def trainNB0(trainmatrix,traincategory):
	numtraindocs = len(trainmatrix)
	numwords = len(trainmatrix[0])
	pabusive = sum(traincategory)/float(numtraindocs)
	p0num = ones(numwords)
	p1num = ones(numwords)
	p0denom = 2.0
	p1denom = 2.0
	for i in range(numtraindocs):
		if traincategory[i] == 1:
		    p1num += trainmatrix[i]
		    p1denom += sum(trainmatrix[i])
		else:
		    p0num += trainmatrix[i]
		    p0denom += sum(trainmatrix[i])
	p1vect = p1num/p1denom
	p0vect = p0num/p0denom
	return p0vect,p1vect,pabusive

def classifyNB(vec2classify,p0vec,p1vec,pclass1):
	p1 = sum(vec2classify * log(p1vec)) + log(pclass1)
	p0 = sum(vec2classify * log(p0vec)) + log(1.0-pclass1)
	if p1 > p0:
	    return 1
	else:
	    return 0


def spamtest():
	doclist = []
	classlist = []
	fulltext = []
	for i in range(1,26):
		wordlist = loademailfile('./lab5/email/spam/%d.txt'%i)
		doclist.append(wordlist)
		fulltext.extend(wordlist)
		classlist.append(1)
		wordlist = loademailfile('./lab5/email/ham/%d.txt'%i)
		doclist.append(wordlist)
		fulltext.extend(wordlist)
		classlist.append(0)

	return doclist,fulltext,classlist

import feedparser
def loadfromrss(feed):
	data = feed['summary']
	regex = re.compile('\\W*')
	wordlist = regex.split(data)
	return[tok.lower() for tok in wordlist if len(tok)>2]

def classifyNB2(vec2classify,p0vec,p1vec,pclass1):
	        p1 = log(sum(vec2classify * p1vec)) + log(pclass1)
		p0 = log(sum(vec2classify * p0vec)) + log(1.0-pclass1)
		if p1 > p0:
		                   return 1
		else:
		                   return 0
def calcmostfreq(vocablist,fulltext):
	import operator
	freqdict = {}
	for i in vocablist:
	    freqdict[i] = fulltext.count(i)
	sortedfreq = sorted(freqdict.iteritems(),key=lambda asd:asd[1],reverse=True)
	return sortedfreq[:30]

def localwords(feed1,feed0):
	import feedparser
	doclist = []
	classlist = []
	fulltext = []
	minlen = min(len(feed1['entries']),len(feed0['entries']))
	for i in range(minlen):
		wordlist = loadfromrss(feed1['entries'][i])
		doclist.append(wordlist)
		fulltext.extend(wordlist)
		classlist.append(1)
        for i in range(minlen):
		wordlist = loadfromrss(feed0['entries'][i])
		doclist.append(wordlist)
		fulltext.extend(wordlist)
		classlist.append(0)
	vocablist = list(set(fulltext))
	top30words = calcmostfreq(vocablist,fulltext)
	for i in top30words:
		if i[0] in vocablist:
		    vocablist.remove(i[0])
	trainingset = range(11,2*minlen)
	testset = []
	for i in range(10):
		randindex = int(random.uniform(11,len(trainingset)))
		testset.append(trainingset[randindex])
		del(trainingset[randindex])
	trainmat = []
	trainclasses = []
	for docindex in trainingset:
	    trainmat.append(bagofwords2vecmn(vocablist,doclist[docindex]))
	    trainclasses.append(classlist[docindex])
	p0v,p1v,pspam = trainNB0(array(trainmat),array(trainclasses))
	return doclist,classlist,fulltext,vocablist,trainingset,testset,p0v,p1v,pspam,trainmat,trainclasses

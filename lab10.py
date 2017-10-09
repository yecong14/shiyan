#!/bin/usr/env python3
from BeautifulSoup import BeautifulSoup
from numpy import *

def scrapepage(retX,retY,infile,yr,numpce,origprc):
    fr = open(infile)
    soup = BeautifulSoup(fr.read())
    i = 1
    currentrow = soup.findAll('table',r='%d'%i)
    while(len(currentrow)!=0):
        currentrow = soup.findAll('table',r='%d'%i)
	title = currentrow[0].findAll('a')[1].text
	lwrtitle = title.lower()
	if (lwrtitle.find('new')>-1) or (lwrtitle.find('nisb')>-1):
		newflag = 1.0
	else:
	        newflag = 0.0
	soldunicde = currentrow[0].findAll('td')[3].findAll('span')
	if len(soldunicde)==0:
	    print('item #%d did not sell'%i)
	else:
	    soldprice = currentrow[0].findAll('td')[4]
	    pricestr = soldprice.text
	    pricestr = pricestr.replace('$','').replace(',','')
	    if len(soldprice)>1:
	        pricestr = pricestr.replace('Free shipping','')
	    sellingprice = float(pricestr)
	    if sellingprice > origprc*0.5:
	        print('%d\t%d\t%d\t%f\t%f'%(yr,numpce,newflag,origprc,sellingprice))
		retX.append([yr,numpce,newflag,origprc])
		retY.append(sellingprice)
	i += 1
	currentrow = soup.findAll('table',r='%d'%i)


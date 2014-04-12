from pandas import Series, DataFrame
import pandas as pd

def standingsAll():

	df1 = pd.read_csv('IDranks2009.csv')
	
	fullStands = df1
	
	for y in [2010, 2011, 2012, 2013]:
		
		stands = pd.read_csv('IDranks%s.csv' % y)
		
		fullStands = pd.merge(fullStands, stands, how='outer')
		
	fullStands.to_csv('fullIdranks.csv', encoding='utf-8')
	
	return fullStands
	
allStands = standingsAll()


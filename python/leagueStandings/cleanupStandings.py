from pandas import Series, DataFrame
import pandas as pd

def winPCT(record):
	[wVal, lVal, tVal] = [int(s) for s in record.split('-')]
	return (wVal + 0.5 * tVal)/(wVal + lVal + tVal)

def standingsAll():

	df1 = pd.read_csv('IDstandings2009.csv')
	
	fullStands = df1.applymap(str)
	
	fullStands['Win Pct 2009'] = fullStands['Record 2009'].map(lambda x: winPCT(x))

	for y in [2010, 2011, 2012, 2013]:
		
		stands = pd.read_csv('IDstandings%s.csv' % y)
		
		stands['Win Pct %s' % y] = stands['Record %s' % y].map(lambda x: winPCT(x))
		
		fullStands = pd.merge(fullStands, stands, how='outer')
		
	fullStands.to_csv('fullIdStandings.csv', encoding='utf-8')
	
	return fullStands
	
allStands = standingsAll()


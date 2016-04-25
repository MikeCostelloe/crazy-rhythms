import csv
from pandas import Series, DataFrame
import pandas as pd

def readStandings():

	stands = pd.read_csv('owners.csv')

	for i in [0, 1, 2, 3]: #CHANGE THIS WEEKLY

		df = pd.read_csv('Week%s_standings.csv' % i)

		stands = pd.merge(stands, df, on='id', how='outer')
	
	standsA = stands.drop('id', axis=1)
	
	standsB = standsA.set_index('Owner')
	
	fullStands = standsB.T
	
	fullStands.index.names = ['Week']
	
	fullStands.to_csv('2016Standings.csv', encoding='utf-8')
	
	return fullStands


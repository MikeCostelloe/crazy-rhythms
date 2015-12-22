import csv
from pandas import Series, DataFrame
import pandas as pd

def readStandings():

	stands = pd.read_csv('owners.csv')

	for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 19, 20]: #CHANGE THIS WEEKLY

		df = pd.read_csv('standings/Week%s_standings.csv' % i)

		stands = pd.merge(stands, df, on='id', how='outer')
	
	standsA = stands.drop('id', axis=1)
	
	standsB = standsA.set_index('Owner')
	
	fullStands = standsB.T
	
	fullStands.index.names = ['Week']
	
	fullStands.to_csv('2015Standings.csv', encoding='utf-8')
	
	return fullStands
	
readStandings()


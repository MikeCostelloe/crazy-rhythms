import csv
from pandas import Series, DataFrame
import pandas as pd

def readStandings():

	stands = pd.read_csv('owners.csv')

	for i in [1, 2, 3, 4]:

		df = pd.read_csv('standings/Week%s_standings.csv' % i)

		stands = pd.merge(stands, df, on='id', how='outer')
	
	standsA = stands.drop('id', axis=1)
	
	standsB = standsA.set_index('Owner')
	
	fullStands = standsB.T
	
	fullStands.index.names = ['Week']
	
	fullStands.to_csv('2014Standings.csv', encoding='utf-8')
	
	return fullStands
	
allStands = readStandings()


import csv
from pandas import Series, DataFrame
import pandas as pd

def rotoScrape():

	stat1 = pd.read_csv('owners.csv')
			
	cols = ['id', 'Owner']

	df = pd.read_csv('Week3_stats.csv') #CHANGE THIS WEEKLY

	stat2 = pd.merge(stat1, df, on='id', how='outer')

	stat = stat2.drop(['BLANK1', 'BLANK2', 'BLANK3'], axis=1)

	points = range(1, 11)

	for c in ['R', 'HR', 'TB', 'RBI', 'SBN', 'OBP', 'IP', 'K', 'SV', 'K-BB']:
	
		stat = stat.sort_index(by='%s' % c)
	
		stat['%s' % c] = points
	
	for c in ['ERA', 'WHIP']:

		stat = stat.sort_index(by='%s' % c, ascending=False)
	
		stat['%s' % c] = points
	
	stat = stat.drop(['id', 'LAST', 'MOVES'], axis=1)

	stat = stat.set_index('Owner')
	
	stat['TOTAL'] = stat.sum(axis=1)

	stat = stat.sort_index(by='TOTAL', ascending=False)

	stat.to_csv('roto2016.csv', encoding='utf-8')
import csv
from pandas import Series, DataFrame
import pandas as pd

def combineStats():
	
	for c in ['R', 'HR', 'TB', 'RBI', 'SBN', 'OBP', 'IP', 'K', 'SV', 'ERA', 'WHIP', 'K-BB', 'LAST', 'MOVES']:
		
			stat = pd.read_csv('owners.csv')
			
			cols = ['id', 'Owner']

			for w in [1, 2, 3, 4]:
			
				cols.append('%s' % w)

				df = pd.read_csv('stats/Week%s_stats.csv' % w)
			
				df1 = df[['id', '%s' % c]].copy()

				stat = pd.merge(stat, df1, on='id', how='outer')
				
				stat.columns = [cols]
			
			statA = stat.drop('id', axis=1)
	
			statB = statA.set_index('Owner')
	
			fullStat = statB.T
	
			fullStat.index.names = ['Week']
	
			fullStat.to_csv('%s.csv' % c, encoding='utf-8')
	
allStats = combineStats()


from urllib2 import urlopen
from bs4 import BeautifulSoup
from pandas import Series, DataFrame
import csv

def cleanNames(record):
	name = record.encode('utf-8')
	return name.split(',', 1)[0]

def projScrape(year, index):

	url = 'http://games.espn.go.com/flb/tools/projections?leagueId=30635&seasonId=' + str(year) + '&startIndex=' + str(index)

	page = urlopen(url)

	soup = BeautifulSoup(page)

	stats = soup.find('table', attrs={'id': 'playertable_0'})

	def categories(row):
		titles = row.findAll('td')
		return [val.text for val in titles]

	def unpack(row):
		cols = row.findAll('td')
		return [val.text for val in cols]

	def parse_stats(table):
			rows = table.findAll('tr')
			header = categories(rows[1])
			data = [unpack(r) for r in rows[2:]]
			return DataFrame(data, columns=header)

	rawData = parse_stats(stats)
	
	statData = rawData.drop(['ACTION'], axis=1)
	
	return statData

def printProj():
	
	years = [2009, 2010, 2011, 2012, 2013, 2014]
	
	for y in years:

		page1 = projScrape(y, 0) 

		page2 = projScrape(y, 40)

		page3 = projScrape(y, 80)

		combined = page1.append([page2, page3], ignore_index=True)
		
		combined['PLAYER, TEAM POS'] = combined['PLAYER, TEAM POS'].map(lambda x: cleanNames(x))

		combined.to_csv('projections%s.csv' % y, encoding='utf-8')
		
		#return combined
		
printProj()
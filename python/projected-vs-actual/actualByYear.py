from urllib2 import urlopen
from bs4 import BeautifulSoup
from pandas import Series, DataFrame
import csv

def statScrape(year, index):

	url = 'http://espn.go.com/mlb/stats/batting/_/year/' + str(year) + '/league/al/count/' + str(index) + '/qualified/true'

	page = urlopen(url)

	soup = BeautifulSoup(page)

	stats = soup.find('table', attrs={'class': 'tablehead'})

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

	statData = parse_stats(stats)
	
	return statData

def printStats():
	
	years = [2009, 2010, 2011, 2012, 2013]
	
	for y in years:

		page1 = statScrape(y, 0)

		page2 = statScrape(y, 41)

		fullData = page1.append(page2, ignore_index=True)

		fullData.to_csv('stats%s.csv' % y, encoding='utf-8')
	
printStats()
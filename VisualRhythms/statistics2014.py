from urllib2 import urlopen
from bs4 import BeautifulSoup
from pandas import Series, DataFrame
import csv

def statScrape():

	url = 'http://games.espn.go.com/flb/standings?leagueId=30635&seasonId=2014'

	page = urlopen(url)

	soup = BeautifulSoup(page)

	stats = soup.find('table', attrs={'id':'statsTable'})
	
	#Strip unique team ID out of each team URL
	def getID(row):
		cols = row.findAll('td')
		link = cols[1].find('a').get('href')
		id = link.split('&', 2)[1]
		return id

	def unpack(row):
		cols = row.findAll('td')
		return [val.text for val in cols[2:]]

	def parse_stats(table):
			rows = table.findAll('tr')
			ids = [getID(r) for r in rows[3:]]
			data = [unpack(r) for r in rows[3:]]
			return DataFrame(data, index=ids, columns=['BLANK1', 'R', 'HR', 'TB', 'RBI', 'SBN', 'OBP', 'BLANK2', 'IP', 'K', 'SV', 'ERA', 'WHIP', 'K-BB', 'BLANK3', 'LAST', 'MOVES'] )

	statData = parse_stats(stats)
	
	statData.to_csv('Week4_stats.csv', encoding='utf-8')
	
	return statData

statScrape()
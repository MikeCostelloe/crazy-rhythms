from urllib2 import urlopen
from bs4 import BeautifulSoup
from pandas import Series, DataFrame
import csv

def standScrape():
	#Strip unique team ID out of each team URL
	def getID(row):
		cols = row.findAll('td')
		link = cols[0].find('a').get('href')
		id = link.split('&', 2)[1]
		return id
	
	#Get team record
	def getRecord(row):
		cols = row.findAll('td')
		record = cols[4].text
		return record
		
	#Build a Dataframe for pairing team ID and record 
	def parse_stats(table):
			rows = table.findAll('tr')
			ids = [getID(r) for r in rows[2:]]
			records = [getRecord(r) for r in rows[2:]]
			return DataFrame(records, index=ids, columns=['20']) #CHANGE THIS WEEKLY
	
	#league URL with with the embedded string for year
	url = 'http://games.espn.go.com/flb/standings?leagueId=30635&seasonId=2015'

	page = urlopen(url)

	soup = BeautifulSoup(page)

	stats = soup.find('table', attrs={'class':'tableBody'})

	standData = parse_stats(stats)
	
	#Print each year to a CSV
	standData.to_csv('Week20_standings.csv', encoding='utf-8') #CHANGE THIS WEEKLY
	
	return standData
	
standScrape()
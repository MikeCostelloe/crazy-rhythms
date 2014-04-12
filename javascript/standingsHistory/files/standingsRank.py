from urllib2 import urlopen
from bs4 import BeautifulSoup
from pandas import Series, DataFrame
import csv

def rankScrape():
	#Iterate through each year of our league
	for y in [2009, 2010, 2011, 2012, 2013]:
		
		#Strip unique team ID out of each team URL
		def getID(row):
			cols = row.findAll('td')
			link = cols[1].find('a').get('href')
			id = link.split('&', 2)[1]
			return id
		
		#Get team record
		def getRecord(row):
			cols = row.findAll('td')
			record = cols[0].text
			return record
			
		#Build a Dataframe for pairing team ID and record 
		def parse_stats(table):
				rows = table.findAll('tr')
				ids = [getID(r) for r in rows[2:]]
				records = [getRecord(r) for r in rows[2:]]
				return DataFrame(records, index=ids, columns=['Rank %s' % y])
		
		#league URL with with the embedded string for year
		url = 'http://games.espn.go.com/flb/tools/finalstandings?leagueId=30635&seasonId=' + str(y)

		page = urlopen(url)

		soup = BeautifulSoup(page)

		stats = soup.find('table', attrs={'id': 'finalRankingsTable'})
	
		standData = parse_stats(stats)
		
		#Print each year to a CSV
		standData.to_csv('IDranks%s.csv' % y, encoding='utf-8')
		
rankScrape()
#Scripts
from standings2016 import standScrape
from combineStandings import readStandings
from statistics2016 import statScrape
from combineStats import combineStats
from roto2016 import rotoScrape

standScrape()

statScrape()

readStandings()

combineStats()

rotoScrape()
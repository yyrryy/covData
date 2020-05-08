import bs4
from bs4 import BeautifulSoup
import requests
import csv



#for data vis.
import matplotlib.pyplot as pl 
import matplotlib.dates as mpld
import pandas as pd
import mplcursors
from datetime import datetime, timedelta
import numpy as np
from matplotlib.widgets import Cursor
import plotly.graph_objects as go




URL1 = 'https://covid.hespress.com/'
URL2 = 'http://www.covidmaroc.ma/Pages/AccueilAR.aspx'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
}
covhes = requests.get(URL1, headers=headers)
covmin = requests.get(URL2, headers=headers)

souprigions = bs4.BeautifulSoup(covhes.content, "html.parser")
soupstats = bs4.BeautifulSoup(covmin.content, "html.parser")



	
when = soupstats.find('td',{'style':'border: 0px solid red; height: 250px; padding-top: 145px; padding-right: 180px; padding-left: 210px;'})
stats = soupstats.find_all("td",{'style':'border: 0px solid red; width: 216px; height: 200px;'})



covData = open('covdata.csv','a')
rigionsData = open('rigions.csv', 'a')


covwriter = csv.writer(covData)
rigwriter = csv.writer(rigionsData)



#CASES
for i in stats:
	time = when.p.text.split()[1].strip('u\u200b')
	date = when.p.text.split()[2]

	total_effected = stats[1].p.text

	recovered = stats[0].p.span.text

	deathstats = soupstats.find('span', {'style':'text-decoration: none solid #b10026;'}).get_text()
	death = ''.join(filter(str.isdigit, deathstats))

	effected = int(total_effected)-int(recovered)-int(death)

	negative = stats[2].p.text

	total_tests = int(total_effected) + int(negative)


#RIGIONS CASES
rig = souprigions.find_all('tr')
for i in rig:
	bnimlal = rig[4].td.text
	casa = rig[0].td.text
	draa = rig[7].td.text
	da5la = rig[11].td.text
	fas = rig[1].td.text
	glmim = rig[6].td.text
	layon = rig[10].td.text
	mrakx = rig[3].td.text
	orio = rig[9].td.text
	rbat = rig[8].td.text
	sous = rig[5].td.text
	tanja = rig[2].td.text


#uncomment out these to append data in the CSVs
#covwriter.writerow([time, date, effected, total_effected, recovered, death, negative, total_tests])
#covData.close()

#rigwriter.writerow([date, bnimlal, casa, draa, da5la, fas, glmim, layon, mrakx, orio, rbat, sous, tanja])
#rigionsData.close()


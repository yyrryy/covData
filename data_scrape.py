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




URL = 'http://www.covidmaroc.ma/Pages/AccueilAR.aspx'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
}
page = requests.get(URL, headers=headers)

soup = bs4.BeautifulSoup(page.content, "html.parser")		
when = soup.find('td',{'style':'border: 0px solid red; height: 250px; padding-top: 145px; padding-right: 180px; padding-left: 210px;'})
stats = soup.find_all("td",{'style':'border: 0px solid red; width: 216px; height: 200px;'})

csv_file = open('covdata.csv','a')

csv_writer = csv.writer(csv_file)

 
#DATE
#date = [] date.append(when.p.text.split()[2])

#TOTAL CONFIRMED
for i in stats:
	time = when.p.text.split()[1].strip('u\u200b')
	date = when.p.text.split()[2]

	total_effected = stats[1].p.text

	recovered = stats[0].p.span.text

	deathstats = soup.find('span', {'style':'text-decoration: none solid #b10026;'}).get_text()
	death = ''.join(filter(str.isdigit, deathstats))

	active = int(total_effected)-int(recovered)-int(death)

	negative = stats[2].p.text

	total_tests = int(total_effected) + int(negative)

"""
#ma5damx ba9i hada
rig = soup.find_all('h2', {'class':'ms-rteElement-H2B'})

for i in rig:
	bni = rig[1].text
	casa  = rig[3].text
	draa = rig[4].text.strip('u\u200b%')
	dak = rig[6].text.strip('u\u200b%')
	fas = rig[8].text
	glmim = rig[10].text.strip('u\u200b%')
	layon = rig[12].text.strip('u\u200b%')
	mrrakx = rig[14].text
	orio = rig[16].text.strip('u\u200b%')
	rrbat = rig[18].text.strip('u\u200b%')
	sos = rig[20].text.strip('u\u200b%')
	tanja = rig[22].text
"""
csv_writer.writerow([time, date, active, total_effected, recovered, death, negative, total_tests])

csv_file.close()

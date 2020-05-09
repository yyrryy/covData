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




Today = date.today().strftime('%d-%m-%Y')
#print(today)
URL1 = 'https://covid.hespress.com/fr'
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
rig_str = []
for n in rig:
    rig_str.append(str(n))

Casa = [i for i, s in enumerate(rig_str) if 'Casablanca' in s]
CasaCases = rig[int(' '.join(str(x) for x in Casa))].td.text

Tanger = [i for i, s in enumerate(rig_str) if 'Tanger' in s]
TangerCases = rig[int(' '.join(str(x) for x in Tanger))].td.text

Fés = [i for i, s in enumerate(rig_str) if 'Fès' in s]
FésCases = rig[int(' '.join(str(x) for x in Fés))].td.text

Béni = [i for i, s in enumerate(rig_str) if 'Béni' in s]
BéniCases = rig[int(''.join(str(x) for x in Béni))].td.text

Marrakech = [i for i, s in enumerate(rig_str) if 'Marrakech' in s]
MarrakechCases = rig[int(''.join(str(x) for x in Marrakech))].td.text

Souss = [i for i, s in enumerate(rig_str) if 'Souss' in s]
SoussCases = rig[int(''.join(str(x) for x in Souss))].td.text

Guelmim = [i for i, s in enumerate(rig_str) if 'Guelmim' in s]
GuelmimCases = rig[int(''.join(str(x) for x in Guelmim))].td.text

Drâa = [i for i, s in enumerate(rig_str) if 'Drâa' in s]
DrâaCases = rig[int(''.join(str(i) for i in Drâa))].td.text

Rabat = [i for i, s in enumerate(rig_str) if 'Rabat' in s]
RabatCases = rig[int(''.join(str(i) for i in Rabat))].td.text

Oriental = [i for i, s in enumerate(rig_str) if 'Oriental' in s]
OrientalCases = rig[int(''.join(str(i) for i in Oriental))].td.text

Laâyoune = [i for i, s in enumerate(rig_str) if 'Laâyoune' in s]
LaâyouneCases = rig[int(''.join(str(i) for i in Laâyoune))].td.text

Dakhla = [i for i, s in enumerate(rig_str) if 'Dakhla' in s]
DakhlaCases = rig[int(''.join(str(i) for i in Dakhla))].td.text


#uncomment out these to append data in the CSVs
#covwriter.writerow([time, date, effected, total_effected, recovered, death, negative, total_tests])
#covData.close()

#rigwriter.writerow([Today, BéniCases, CasaCases, DrâaCases, DakhlaCases, FésCases, GuelmimCases, LaâyouneCases, MarrakechCases, OrientalCases, RabatCases, SoussCases, TangerCases])
#rigionsData.close()


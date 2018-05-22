import urllib2
from bs4 import BeautifulSoup

ur1='https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting'

source=urllib2.urlopen(ur1)

soup=BeautifulSoup(source)
all_tables=soup.find_all('table')

right_table=soup.find('table', class_='table rankings-table')

A=[]
B=[]
C=[]
D=[]
for i in right_table.findAll('tr'):
    cells=i.findAll('td')
    if cells != []:
        if len(cells) == 3:
            a =  cells[1].text.strip()
            b = a.split()
            name = ' '.join(b[:-1])
            team = b[-1]
            A.append(cells[0].text.strip())
            B.append(name)
            C.append(team)
            D.append(cells[2].text.strip())
        else:
            A.append(cells[0].text.strip())
            B.append(cells[1].text.strip())
            C.append(cells[2].text.strip())
            D.append(cells[3].text.strip())
        

import pandas as pd
df=pd.DataFrame(A,columns=['position'])
df['player']=B
df['country']=C
df['rating']=D


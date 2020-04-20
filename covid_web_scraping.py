import os
import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup

directory = os.environ['HOMEPATH'] + '/Documents/Covid Folder'

if os.path.exists(directory):
    try:
        os.makedirs(directory)
        print('Directory is successfully created!')
    except OSError:
        print('Creation of the directory failed')

url_confirmed = urlopen('https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')

bs_confirmed = BeautifulSoup(url_confirmed,'html.parser')

tabletag_confirmed = bs_confirmed.select('table')[0]

df_confirmed = pd.read_html(str(tabletag_confirmed))[0]

df_confirmed.to_csv(directory + '/covid_data.csv', index=True, header=True)


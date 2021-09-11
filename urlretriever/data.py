import os
import pandas as pd

from urllib.request import urlretrieve

Fremont_bridge_URL = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'
#URL2 = 'https://data.seattle.gov/api/views/38vd-gytv/rows.csv?accessType=DOWNLOAD'

#function to retrieve data from internet using url link
#""" Download and cache the url from online """

def get_fremont_data (filename = 'Fremont_bridge.csv', url = Fremont_bridge_URL, force_download = False ):
    if force_download or not os.path.exists (filename):
        urlretrieve(url, filename)
    data = pd.read_csv ('Fremont_bridge.csv', index_col = 'Date', parse_dates = True)
    return data

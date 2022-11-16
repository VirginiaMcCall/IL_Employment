import urllib.request
import pandas as pd
import sqlalchemy as sa
from DataLink import engine

#Opens Url 
webUrl = urllib.request.urlopen('https://data.illinois.gov/datastore/dump/1a0cd05c-7d17-4e3d-938d-c2bfa2a4a0b1')  

#Creates DataFrame using pandas to read csv file from url
df = pd.read_csv(webUrl)
print(df)

#Added code to enable writing to SQL database. 
df.to_sql('HR_DATA',con=engine, schema='dbo', if_exists='replace',index=True) 
 

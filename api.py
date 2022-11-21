from datetime import datetime
import pandas as pd
import requests
from pathlib import Path

#website = https://finnhub.io/docs/api/introduction (sign up GET FREE API KEY)

#repository github examples = https://github.com/Finnhub-Stock-API/finnhub-python/blob/master/examples.py

stk_ticker = 'AAPL'
data_resolution = 'W' # weekly
timestamp_from = 1667347107 
timestamp_to = 1668556707
API_Key = ''# enter the api_key here
Address_template = 'https://finnhub.io/api/v1/stock/candle?symbol={}&resolution={}&from={}&to={}&token={}'

API_address = Address_template.format(stk_ticker, data_resolution, timestamp_from, timestamp_to, API_Key)


r = requests.get(API_address)

AAPL_df=pd.DataFrame(r.json())
AAPL_df.drop(columns='s',inplace=True)
AAPL_df.t = AAPL_df.t.apply(datetime.fromtimestamp)
AAPL_df.t =AAPL_df.t.apply(lambda v:v.date())
AAPL_df.set_index('t',drop=True,inplace=True)
AAPL_df.columns=['Closing','High','Low','Opening','Volume']

print(AAPL_df.head())

#path="C:\Users\cafra\OneDrive\Documents\Learn Books\Hands-On Data  Preprocessing in python"
AAPL_df.to_csv('appl.csv')








print(r)
print(r.json())


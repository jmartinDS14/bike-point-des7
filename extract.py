import requests
import json
import os
from datetime import datetime
import time
import logging

url = 'https://api.tfl.gov.uk/BikePoint/'
data_dir = 'data'
os.makedirs(data_dir,exist_ok=True)
timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
filename = f'{data_dir}/{timestamp}.json'
max_retry = 5
attempt = 0
delay = 10

response = requests.get(url)
data = response.json()

with open(filename,'w') as file:
    json.dump(data,file)
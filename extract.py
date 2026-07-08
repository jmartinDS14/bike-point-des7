import requests
import json
import os
from datetime import datetime
import time
import logging

timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
log_dir = 'logs'
os.makedirs(log_dir,exist_ok=True)
log_filename = f'{log_dir}/{timestamp}.log'

logging.basicConfig(
    filename=log_filename,
    format = '%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger=logging.getLogger()
logger.info('Logger successfully initialised')

url = 'https://api.tfl.gov.uk/BikePoint/'
data_dir = 'data'
os.makedirs(data_dir,exist_ok=True)
filename = f'{data_dir}/{timestamp}.json'
max_retry = 5
attempt = 0
delay = 10

while attempt < max_retry:
    response = requests.get(url)
    status = response.status_code
    if 200 <= status < 300:
        data = response.json()
        if len(data) > 0:
            try:
                with open(filename,'w') as file:
                    json.dump(data,file)
                print('yay 🎉')
                logger.info(f'File {filename} was successfully saved')
            except Exception as e:
                logger.error(f'An error occurred: {e}')
            break
        else:
            logger.error('No data returned')
            break
    elif status<=100 or status>=500:
        time.sleep(delay)
        print('retrying')
        logger.info(f'Status code {status}. Retrying. This was attempt {attempt}')
        attempt+=1
    else:
        print('fix something')
        print(status)
        logger.error(f'Error. Status code {status}. Fix it.')
        break
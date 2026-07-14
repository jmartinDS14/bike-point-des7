import requests
import json
import os
import time
import logging

logger = logging.getLogger(__name__)

def extract_to_json(url:str, data_dir:str, timestamp:str, max_retry:int, delay:int):
    """
    This function calls a specified url. It should be used for APIs which return json. 
    If there's a server side issue it will retry for the specified number of times. 
    The json data will be saved in the specified directory.

    Args:
        url (str): API endpoint to call
        data_dir (str): The name of the directory to save the data to
        timestamp (str): The json file will be named this timestamp value
        max_retry (int): The number of times you would like to retry if there's a server side error
        delay (int): The number of seconds you would like to delay between retries
    """
    os.makedirs(data_dir,exist_ok=True)
    filename = f'{data_dir}/{timestamp}.json'
    attempt = 0

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
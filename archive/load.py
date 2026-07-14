import os
from datetime import datetime
import logging
from dotenv import load_dotenv
import boto3

timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
log_dir = 'logs'
os.makedirs(log_dir,exist_ok=True)
log_filename = f'{log_dir}/load_{timestamp}.log'

logging.basicConfig(
    filename=log_filename,
    format = '%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger=logging.getLogger()
logger.info('Logger successfully initialised')

load_dotenv()

AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_BUCKET_NAME = os.getenv('AWS_BUCKET_NAME')

s3_client = boto3.client(
    's3',
    aws_access_key_id = AWS_ACCESS_KEY,
    aws_secret_access_key = AWS_SECRET_ACCESS_KEY
)

data_dir = 'data'
files = os.listdir(data_dir)

for file in files:
    to_upload = f'{data_dir}/{file}'
    try:
        s3_client.upload_file(to_upload,AWS_BUCKET_NAME,file)
        logger.info(f'{file} successfully uploaded.')
        os.remove(to_upload)
    except Exception as e:
        logger.error(e)
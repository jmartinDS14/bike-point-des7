from datetime import datetime
from dotenv import load_dotenv
import os
from modules.extract_function import extract_to_json
from modules.load_function import load_to_s3
from modules.logging_function import setup_logger

timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
log_dir = 'logs'

logger = setup_logger(timestamp,log_dir)
logger.info('Logger initialised')

url = 'https://api.tfl.gov.uk/BikePoint/'
data_dir = 'data'

extract_to_json(
    url,
    data_dir,
    timestamp,
    max_retry=3,
    delay=10
)

load_dotenv()

AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_BUCKET_NAME = os.getenv('AWS_BUCKET_NAME')

load_to_s3(
    AWS_ACCESS_KEY,
    AWS_SECRET_ACCESS_KEY,
    AWS_BUCKET_NAME,
    data_dir
)
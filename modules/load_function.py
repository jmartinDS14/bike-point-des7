import os
import logging
import boto3

logger = logging.getLogger(__name__)

def load_to_s3(AWS_ACCESS_KEY:str, AWS_SECRET_ACCESS_KEY:str, AWS_BUCKET_NAME:str, data_dir:str):
    """
    This function will load any json files in the data directory to a specified S3 bucket.

    Args:
        AWS_ACCESS_KEY (str): The AWS access key ID attached to an IAM User, with relevant permissions.
        AWS_SECRET_ACCESS_KEY (str): The AWS secret access key attached to an IAM User, with relevant permissions.
        AWS_BUCKET_NAME (str): The name of the S3 bucket
        data_dir (str): The name of the directory where the json files are located
    """
    s3_client = boto3.client(
        's3',
        aws_access_key_id = AWS_ACCESS_KEY,
        aws_secret_access_key = AWS_SECRET_ACCESS_KEY
    )

    files = os.listdir(data_dir)

    for file in files:
        to_upload = f'{data_dir}/{file}'
        try:
            s3_client.upload_file(to_upload,AWS_BUCKET_NAME,file)
            logger.info(f'{file} successfully uploaded.')
            os.remove(to_upload)
        except Exception as e:
            logger.error(e)
import logging
import os

def setup_logger(timestamp:str,log_dir:str):
    """
    This initialises the logger for everything.

    Args:
        timestamp (str): For the filenames of the logs.
        log_dir (str): Where the logs should be stored.
    """
    os.makedirs(log_dir,exist_ok=True)
    log_filename = f'{log_dir}/{timestamp}.log'

    logging.basicConfig(
        filename=log_filename,
        format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )

    return logging.getLogger()
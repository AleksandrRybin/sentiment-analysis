import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)s: %(message)s', 
    datefmt='%d-%b-%y %H:%M:%S',
    level=logging.INFO
)

from .app import app
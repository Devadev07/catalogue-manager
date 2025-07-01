import mysql.connector
from configparser import ConfigParser
import os

def get_db():
    config = ConfigParser()
    config.read(os.path.join(os.path.dirname(__file__), '../config/config.ini'))
    return mysql.connector.connect(
        host=config['mysql']['host'],
        user=config['mysql']['user'],
        password=config['mysql']['password'],
        database=config['mysql']['database']
    )

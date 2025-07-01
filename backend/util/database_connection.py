import mysql.connector
from configparser import ConfigParser

def get_db():
    config = ConfigParser()
    config.read('backend/config/config.ini')
    db = mysql.connector.connect(
        host=config['mysql']['host'],
        user=config['mysql']['user'],
        password=config['mysql']['password'],
        database=config['mysql']['database']
    )
    return db

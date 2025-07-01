import mysql.connector
import configparser
import os

def get_db():
    config = configparser.ConfigParser()
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.ini')
    config.read(config_path)
    db_config = config['mysql']
    return mysql.connector.connect(
        host=db_config['host'].replace("'", "").replace(",", "").strip(),
        user=db_config['user'].replace("'", "").replace(",", "").strip(),
        password=db_config['password'].replace("'", "").replace(",", "").strip(),
        database=db_config['database'].replace("'", "").replace(",", "").strip()
    )
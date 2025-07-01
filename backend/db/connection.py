import mysql.connector

def get_db():
    return mysql.connector.connect(
        host='localhost',
        user='root', 
        password='8055', 
        database='companydb' 
    )

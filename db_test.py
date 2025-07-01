import mysql.connector

try:
    connection = mysql.connector.connect(
        host='localhost',
        user='root',  
        password='8055',
        database='companydb'  
    )

    if connection.is_connected():
        print("✅ Successfully connected to the MySQL database!")
    else:
        print("❌ Connection failed.")

    connection.close()

except mysql.connector.Error as err:
    print(f"❌ Error: {err}")

# Install MySQL on your computer
# pip install mysql
# pip install mysql-connector

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'kaushik',
    passwd = 'kaushik'

)

# prepare a cursor object
cusorObject = dataBase.cursor()

# create a database
cusorObject.execute("CREATE DATABASE elderco")

print("All Done!")


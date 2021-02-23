import mysql.connector

db2 = mysql.connector.connect(
    host="localhost",
    user="root",
    password="project1"
)

db2Cursor = db2.cursor()
db2Cursor.execute("CREATE DATABASE testdatabase")

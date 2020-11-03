import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="project1"
)

print(mydb)
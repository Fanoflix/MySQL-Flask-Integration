import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="project1",
  database="projdatabase" # ONLY add this line after the database has been CREATED!
)


dbCursor = mydb.cursor()

#### -- CREATE DATABASE -- ####
# # dbCursor.execute("CREATE DATABASE projadatabase")  # Run once

#### -- CHECK TO SEE IF DB EXISTS -- ####
# dbCursor.execute("SHOW DATABASES")  # Run in conjunction with the for loop below
# for x in dbCursor:  # prints information about the DB.
#     print(x)

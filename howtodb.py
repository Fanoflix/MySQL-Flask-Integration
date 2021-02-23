import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="project1",
  database="testdb" # ONLY add this line after the database has been CREATED!
)

#### -- SET CURSOR # run always!
dbCursor = mydb.cursor()

#### -- CREATE DATABASE -- ####
# dbCursor.execute("CREATE DATABASE testdb")  # Run once

#### -- CHECK TO SEE IF DB EXISTS -- ####
# dbCursor.execute("SHOW DATABASES")  # Run in conjunction with the for loop below
# for x in dbCursor:  # prints information about the DB.
#     print(x)

### -- CREATE TABLE --- ###
# dbCursor.execute("CREATE TABLE employees (id INT AUTO_INCREMENT PRIMARY KEY, fname VARCHAR(25), lname VARCHAR(25), department VARCHAR(255))")

### -- ALTER --- ###
# dbCursor.execute("ALTER TABLE testtable ADD COLUMN age INT")

### -- INSERT (WAY 1) --- ###
# sql = "INSERT INTO employees (fname, lname, department) VALUES (%s, %s, %s)"
# vals = ("Mahad", "Khalid", "CS")
# dbCursor.execute(sql, vals) # You can use .executemany() if the "vals" contains multiple values, instead use .execute

### -- INSERT (WAY 2) # Insert info from Variable --- ###
idd = dbCursor.lastrowid
fnamed = "Faizan"
lnamed= "Shahid"
departmentd = "CS"
dbCursor.execute("""
INSERT INTO employees (fname, lname, department)
VALUES (%(fname)s, %(lname)s, %(department)s) 
""",
{
  "fname" : fnamed,
  "lname" : lnamed,
  "department" : departmentd
})

### --- DELETE RECORD ---
dbCursor.execute("DELETE FROM employees WHERE id = 6 ")
# ### -- COMMIT --- ### Always commit after changes
# mydb.commit()


### -- SELECT ---
dbCursor.execute("SELECT * FROM employees")
result = dbCursor.fetchall() # Fetch whatever the SQL Query returned

## -- PRINT ---
# Iterating over the result array and printing its content.
print('-------------------------------------------------')
for x in result:
    print(x)
print('-------------------------------------------------')

## SHOW ALL EXISTING TABLES
# dbCursor.execute("SHOW TABLES")
# for x in dbCursor:
#     print(x)

## CLOSE CURSOR AND CONNECTION
# dbCursor.close()
# mydb.close()
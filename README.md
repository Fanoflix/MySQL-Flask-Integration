# MySQL-Flask Integration
 Integrating MySQL with Flask

## Setting up Database (Commit # 3: Setting up Database)
### Setting up
##### Note: Check code in the commit for better understanding.

- Download MySQL and set up a connection

- Connect to the MySQL connection using the host, username and password.

- Set up a Cursor
---
     WHAT IS CURSOR?

    -The MySQLCursor class instantiates objects that 
    can execute operations such as SQL statements. 
    Cursor objects interact with the MySQL server 
    using a MySQLConnection object. 
---
- Create Databse using <cursor_name>.execute("CREATE DATABASE <db_name>")

- Run this code once and make sure theres no error

- Remove lines commented with "Run once" and add the line:
database = "<db_name>" to the connector.
###
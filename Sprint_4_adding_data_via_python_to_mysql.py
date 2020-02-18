#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
print('-'*10 + "Welcome to Data Vault" + '-'*10)
print("\nThis is the original data")
df=pd.read_csv("Data_Vault_Final1.csv")
df


# In[17]:


import mysql.connector
db_connection = mysql.connector.connect(
 host="localhost",
 user="root",
 passwd="Easy2020!",
 database="mydatabase"
 )
db_cursor = db_connection.cursor()
#products_sql_query = "INSERT INTO data_vault_final1(products,type,price,quantity)VALUES('Bakery', 'bread', 15, 40)"
#employee_sql_query = " INSERT INTO employee (id, name, salary) VALUES (01, 'John', 10000)"
#Execute cursor and pass query 
db_cursor.execute("INSERT INTO data_vault_final1(products,type,price,quantity)VALUES('Bakery', 'bread', 15, 40)")
#Execute cursor and pass query of employee and data of employee
#db_cursor.execute(employee_sql_query)
db_connection.commit()
print(db_cursor.rowcount, "Record Inserted")


# In[28]:


import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
import mysql.connector
db_connection = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Easy2020!",
  database="mydatabase"
  )
mycursor = mydb.cursor()
mycursor.execute("ALTER TABLE data_vault_final1 ADD barcode VARCHAR(50) NOT NULL AFTER quantity;")

#mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")


# In[29]:


import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
import mysql.connector
db_connection = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Easy2020!",
  database="mydatabase"
  )
mycursor = mydb.cursor()
# This script adds another column in the table
mycursor.execute("ALTER TABLE data_vault_final1 ADD expiry_date VARCHAR(50) NOT NULL AFTER barcode;")


# In[ ]:


import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
import mysql.connector
db_connection = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Easy2020!",
  database="mydatabase"
  )
mycursor = mydb.cursor()
# This script adds another column in the table
mycursor.execute("ALTER TABLE data_vault_final1 ADD expiry_date VARCHAR(50) NOT NULL AFTER barcode;")


# In[30]:


import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
import mysql.connector
db_connection = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Easy2020!",
  database="mydatabase"
  )
mycursor = mydb.cursor()
# This script adds another column in the table
mycursor.execute("ALTER TABLE data_vault_final1 ADD purchased VARCHAR(50) NOT NULL AFTER barcode;")


# In[ ]:


import mysql.connector
db_connection = mysql.connector.connect(
 host="localhost",
 user="root",
 passwd="Easy2020!",
 database="mydatabase"
 )
db_cursor = db_connection.cursor()
db_cursor.execute("INSERT INTO data_vault_final1(products,barcode)VALUES('Bakery', 'bread', 15, 40)")
db_connection.commit()
print(db_cursor.rowcount, "Record Inserted")


# In[2]:


import mysql.connector
import MySQLdb as sql

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Easy2020!",
  database="mydatabase"
)

#mycursor = mydb.cursor()
mycursor = mydb.cursor()
sql = "UPDATE data_vault_final1 SET barcode = '10002020' WHERE type = 'Lays'" # this script updates the barcode in the database
mycursor.execute(sql)
print(mycursor.rowcount, "record(s) affected")


# In[3]:


mydb.commit()


# In[4]:


import mysql.connector
import MySQLdb as sql

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Easy2020!",
  database="mydatabase"
)

#mycursor = mydb.cursor()
mycursor = mydb.cursor()
sql = "UPDATE data_vault_final1 SET purchased = '2', expiry_date='18/02/2022' WHERE type = 'Lays'" # this script updates the barcode in the database
mycursor.execute(sql)
print(mycursor.rowcount, "record(s) affected")


# In[5]:


mydb.commit()


# In[6]:


import mysql.connector
import MySQLdb as sql

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Easy2020!",
  database="mydatabase"
)

#mycursor = mydb.cursor()
mycursor = mydb.cursor()
sql = "UPDATE data_vault_final1 SET barcode='100023352', purchased = '5', expiry_date='18/02/2022' WHERE type = 'Doritos'" # this script updates the barcode in the database
mycursor.execute(sql)
print(mycursor.rowcount, "record(s) affected")


# In[7]:


mydb.commit()


# In[8]:


import mysql.connector
import MySQLdb as sql

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Easy2020!",
  database="mydatabase"
)

#mycursor = mydb.cursor()
mycursor = mydb.cursor()
sql = "UPDATE data_vault_final1 SET barcode='10002335', purchased = '6', expiry_date='18/02/2023' WHERE type = 'Nik naks'" # this script updates the database
mycursor.execute(sql)
print(mycursor.rowcount, "record(s) affected")


# In[9]:


mydb.commit()


# In[10]:


import mysql.connector
import MySQLdb as sql

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Easy2020!",
  database="mydatabase"
)

#mycursor = mydb.cursor()
mycursor = mydb.cursor()
sql = "UPDATE data_vault_final1 SET barcode='20002335', purchased = '20', expiry_date='18/02/2021' WHERE type = 'coke'" # this script updates the database
mycursor.execute(sql)
print(mycursor.rowcount, "record(s) affected")


# In[11]:


mydb.commit()


# In[12]:


import mysql.connector
import MySQLdb as sql

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Easy2020!",
  database="mydatabase"
)

#mycursor = mydb.cursor()
mycursor = mydb.cursor()
sql = "UPDATE data_vault_final1 SET barcode='20002336', purchased = '21', expiry_date='18/03/2021' WHERE type = 'sprite'" # this script updates the database
mycursor.execute(sql)
print(mycursor.rowcount, "record(s) affected")


# In[13]:


mydb.commit()


# In[14]:


import mysql.connector
import MySQLdb as sql

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Easy2020!",
  database="mydatabase"
)

#mycursor = mydb.cursor()
mycursor = mydb.cursor()
sql = "UPDATE data_vault_final1 SET barcode='20002337', purchased = '18', expiry_date='19/03/2021' WHERE type = 'stoney'" # this script updates the database
mycursor.execute(sql)
print(mycursor.rowcount, "record(s) affected")


# In[15]:


mydb.commit()


# In[16]:


import mysql.connector
import MySQLdb as sql

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Easy2020!",
  database="mydatabase"
)

#mycursor = mydb.cursor()
mycursor = mydb.cursor()
sql = "UPDATE data_vault_final1 SET barcode='20002411', purchased = '15', expiry_date='19/02/2021' WHERE type = 'steak & pepper'" # this script updates the database
mycursor.execute(sql)
print(mycursor.rowcount, "record(s) affected")


# In[17]:


mydb.commit()


# In[18]:


import mysql.connector
import MySQLdb as sql

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Easy2020!",
  database="mydatabase"
)

#mycursor = mydb.cursor()
mycursor = mydb.cursor()
sql = "UPDATE data_vault_final1 SET barcode='20002338', purchased = '20', expiry_date='19/03/2021' WHERE type = 'chicken mayo'" # this script updates the database
mycursor.execute(sql)
print(mycursor.rowcount, "record(s) affected")


# In[19]:


mydb.commit()


# In[22]:


import mysql.connector
import MySQLdb as sql

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Easy2020!",
  database="mydatabase"
)

#mycursor = mydb.cursor()
mycursor = mydb.cursor()
sql = "UPDATE data_vault_final1 SET barcode='20002338', purchased = '11', expiry_date='20/03/2021' WHERE type = 'spinach& feta'" # this script updates the database
mycursor.execute(sql)
print(mycursor.rowcount, "record(s) affected")


# In[23]:


mydb.commit()


# In[24]:


import mysql.connector
import MySQLdb as sql

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Easy2020!",
  database="mydatabase"
)

#mycursor = mydb.cursor()
mycursor = mydb.cursor()
sql = "UPDATE data_vault_final1 SET barcode='20002433', purchased = '18', expiry_date='19/03/2020' WHERE type = 'banana'" # this script updates the database
mycursor.execute(sql)
print(mycursor.rowcount, "record(s) affected")


# In[25]:


mydb.commit()


# In[26]:


import mysql.connector
import MySQLdb as sql

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Easy2020!",
  database="mydatabase"
)

#mycursor = mydb.cursor()
mycursor = mydb.cursor()
sql = "UPDATE data_vault_final1 SET barcode='20002338', purchased = '11', expiry_date='19/03/2021' WHERE type = 'apples'" # this script updates the database
mycursor.execute(sql)
print(mycursor.rowcount, "record(s) affected")


# In[27]:


mydb.commit()


# In[28]:


import mysql.connector
import MySQLdb as sql

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Easy2020!",
  database="mydatabase"
)

#mycursor = mydb.cursor()
mycursor = mydb.cursor()
sql = "UPDATE data_vault_final1 SET barcode='20002338', purchased = '12', expiry_date='19/03/2021' WHERE type = 'pears'" # this script updates the database
mycursor.execute(sql)
print(mycursor.rowcount, "record(s) affected")


# In[29]:


mydb.commit()


# In[31]:


import mysql.connector
import MySQLdb as sql

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Easy2020!",
  database="mydatabase"
)

#mycursor = mydb.cursor()
mycursor = mydb.cursor()
sql = "UPDATE data_vault_final1 SET barcode='20002446', purchased = '12', expiry_date='28/02/2020' WHERE type = 'spinach'" # this script updates the database
mycursor.execute(sql)
print(mycursor.rowcount, "record(s) affected")


# In[32]:


mydb.commit()


# In[33]:


import mysql.connector
import MySQLdb as sql

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Easy2020!",
  database="mydatabase"
)

#mycursor = mydb.cursor()
mycursor = mydb.cursor()
sql = "UPDATE data_vault_final1 SET barcode='20002447', purchased = '10', expiry_date='19/03/2020' WHERE type = 'beetrot'" # this script updates the database
mycursor.execute(sql)
print(mycursor.rowcount, "record(s) affected")


# In[34]:


mydb.commit()


# In[35]:


import mysql.connector
import MySQLdb as sql

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Easy2020!",
  database="mydatabase"
)

#mycursor = mydb.cursor()
mycursor = mydb.cursor()
sql = "UPDATE data_vault_final1 SET barcode='20002448', purchased = '9', expiry_date='18/03/2020' WHERE type = 'cabbage'" # this script updates the database
mycursor.execute(sql)
print(mycursor.rowcount, "record(s) affected")


# In[36]:


mydb.commit()


# In[13]:


import mysql.connector
#import MySQLdb as sql

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Easy2020!",
  database="mydatabase"
)

#mycursor = mydb.cursor()
mycursor = mydb.cursor()
sql = "UPDATE data_vault_final1 SET barcode='20002337', purchased = '18', expiry_date='25/02/2020' WHERE type = 'bread'" # this script updates the database
mycursor.execute(sql)
print(mycursor.rowcount, "record(s) affected")


# In[19]:


import mysql.connector
db_connection = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Easy2020!",
  database="mydatabase"
  )
db_cursor = db_connection.cursor()
#products_sql_query = "INSERT INTO data_vault_final1(products,type,price,quantity)VALUES('Bakery', 'bread', 15, 40)"
#employee_sql_query = " INSERT INTO employee (id, name, salary) VALUES (01, 'John', 10000)"
#Execute cursor and pass query 
db_cursor.execute("INSERT INTO data_vault_final1(products,type,price,quantity,barcode,purchased,Expiry_date)VALUES('Bathroom', 'Jik', 15, 40,5223600,25,'22/01/2021')")
#Execute cursor and pass query of employee and data of employee
#db_cursor.execute(employee_sql_query)
db_connection.commit()
print(db_cursor.rowcount, "Record Inserted")


# In[21]:


import mysql.connector
db_connection = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Easy2020!",
  database="mydatabase"
  )
db_cursor = db_connection.cursor()
#products_sql_query = "INSERT INTO data_vault_final1(products,type,price,quantity)VALUES('Bakery', 'bread', 15, 40)"
#employee_sql_query = " INSERT INTO employee (id, name, salary) VALUES (01, 'John', 10000)"
#Execute cursor and pass query 
db_cursor.execute("INSERT INTO data_vault_final1(products,type,price,quantity,barcode,purchased,Expiry_date)VALUES('Bakery', 'hotdogs', 40, 75,522361147,30,'22/01/2022')")
#Execute cursor and pass query of employee and data of employee
#db_cursor.execute(employee_sql_query)
db_connection.commit()
print(db_cursor.rowcount, "Record Inserted")


# In[25]:


import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Easy2020!",
  database="mydatabase"
  )
print('-'*10 + "Welcome to Data Vault" + '-'*10)
#print("\nThis is the original data")
#df=pd.read_csv("Data_Vault_Final1.csv")

chips=pd.read_sql_query("select * from mydatabase.data_vault_final1 where products='chips'",mydb)
chips


# In[28]:



coldrinks=pd.read_sql_query("select * from mydatabase.data_vault_final1 where products='coldrinks'",mydb)
coldrinks


# In[29]:



Bakery=pd.read_sql_query("select * from mydatabase.data_vault_final1 where products='Bakery'",mydb)
Bakery


# In[30]:



fruits=pd.read_sql_query("select * from mydatabase.data_vault_final1 where products='fruits'",mydb)
fruits


# In[31]:



veggies=pd.read_sql_query("select * from mydatabase.data_vault_final1 where products='veggies'",mydb)
veggies


# In[32]:



pie=pd.read_sql_query("select * from mydatabase.data_vault_final1 where products='pie'",mydb)
pie


# In[33]:


bathroom=pd.read_sql_query("select * from mydatabase.data_vault_final1 where products='bathroom'",mydb)
bathroom


# In[ ]:





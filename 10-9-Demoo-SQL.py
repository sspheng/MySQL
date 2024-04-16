import mysql.connector
import pandas as pd
mydb = mysql.connector.connect(host="localhost",user="root",database="classicmodels")
print('connected to employee')
mycursor = mydb.cursor()
#mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)


sql_query = pd.read_sql_query ('''select * from customers ''', mydb)

print(sql_query)

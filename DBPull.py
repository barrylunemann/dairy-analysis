# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sqlite3 as lite
import pyodbc
import pandas as pd

dbcon = lite.connect("C:/tempdb.db")

dbcon = lite.connect("C:/Users/Barrett/Documents/Delpro Files/DDMParlor.db")
#
#conn = pyodbc.connect(r'Driver={SQL Server};Server=TE-DAIRY\DELPRO;Database=DDMParlor;Trusted_Connection=yes;')
#conn = pyodbc.connect(r'Driver={SQL Server};Server=TE-DAIRY\DELPRO;Database=tempdb;Trusted_Connection=yes;')
cursor = conn.cursor()


#test2 = pd.read_sql("SELECT COLUMN_NAME, * FROM INFORMATION_SCHEMA.COLUMNS", dbcon)

counter = 0
testdict = {}

tablenames = []

for rows in cursor.tables():
    tablename = str(rows.table_schem)+"."+str(rows.table_name)
    tablenames.append(tablename)
errorlist = []
try:
    for rows in cursor.tables():
        if counter < 5:
        
            xvariable = str(rows)
            tablename = str(rows.table_schem)+"."+str(rows.table_name)
            x = "SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED SELECT TOP 500 * FROM " + str(rows.table_schem)+"."+str(rows.table_name)
            print(tablename)
            conn = pyodbc.connect(r'Driver={SQL Server};Server=TE-DAIRY\DELPRO;Database=tempdb;Trusted_Connection=yes;')
            try:
                test = pd.read_sql(x, conn)
            except:
                errorlist.append(tablename)
                print('Error on ' + tablename)
                
            print(rows.table_schem)
            testdict[xvariable] = test
            #counter +=1
            test.to_sql(tablename, dbcon, if_exists = 'append', index = False)
                        

except:
    print('Failed')
    
conn.close()
dbcon.close()


test = pd.read_sql("SELECT name FROM sqlite_master WHERE type = 'table'",dbcon)



dbcon = lite.connect("C:/Users/Barrett/Documents/Delpro Files/DDMParlor.db")
test2 = pd.read_sql("SELECT name FROM sqlite_master", dbcon)

output = pd.DataFrame()
for iter in test2.iloc[:,0]:
    x = "SELECT COUNT(*) FROM '" + iter + "'"
    test = pd.read_sql(x, dbcon)
    test['table'] = iter
    output = output.append(test,ignore_index = True)
output = output.sort_values(['COUNT(*)'], ascending = False)

output.to_excel('C:/Users/Barrett/Documents/Delpro Files/master Tables.xlsx', index=False)

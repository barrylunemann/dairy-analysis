# -*- coding: utf-8 -*-
# *** Spyder Python Console History Log ***

## ---(Fri Jun  8 23:21:04 2018)---
import sqlite3 as lite
dbcon = lite.connect("C:/Users/Barrett/Documents/Delpro Files/DDMParlor.db")
cursor = dbcon.cursor()
tablenames = []

for rows in cursor.tables():
    tablename = str(rows.table_schem)+"."+str(rows.table_name)
    tablenames.append(tablename)
    
test = pd.read_sql("SELECT name FROM sqlite_master WHERE type = 'table'",dbcon)
import pandas as pd
test = pd.read_sql("SELECT name FROM sqlite_master WHERE type = 'table'",dbcon)
test.iloc]0,0]
test.iloc[0,0]
test2 = pd.read_sql("SELECT name FROM " + test.iloc[0,0] + " WHERE type = 'table'", dbcon)
dbcon = lite.connect("C:/Users/Barrett/Documents/Delpro Files/DDMParlor.db")
test2 = pd.read_sql("SELECT name FROM " + test.iloc[0,0] + " WHERE type = 'table'", dbcon)
test2 = pd.read_sql("SELECT name FROM " + test.iloc[0,0], dbcon)
test2 = pd.read_sql("SELECT * FROM " + test.iloc[0,0], dbcon)
test2 = pd.read_sql("SELECT * FROM AbstractAnimalConfig", dbcon)
test = pd.read_sql("SELECT name FROM sqlite_master WHERE type = 'table'",dbcon)
test2 = pd.read_sql("SELECT * FROM dbo.CodeSet", dbcon)
test2 = pd.read_sql("SELECT * FROM CodeSet", dbcon)
test2 = pd.read_sql("SELECT * FROM CodeSet", con=dbcon)
test2 = pd.read_sql("SELECT * FROM dbo.CodeSet", con=dbcon)
test2 = pd.read_sql("SELECT * FROM dbo.CodeSet", con = dbcon)
test = pd.read_sql("SELECT name FROM sqlite_master WHERE type = 'table'",dbcon)
test = None
test = pd.read_sql("SELECT name FROM sqlite_master WHERE type = 'table'",dbcon)
cursor = dbcon.cursor()
xtest = cursor.fetchall()
print(xtest)
cur = dbcon.cursor()
xtest = cur.fetchall()
dbcon = lite.connect("C:/Users/Barrett/Documents/Delpro Files/master.db")
test = pd.read_sql("SELECT name FROM sqlite_master WHERE type = 'table'",dbcon)
test2 = pd.read_sql("SELECT * FROM sys.views", con = dbcon)
test2 = pd.read_sql('sys.views', con = dbcon)
test2 = pd.read_sql("SELECT * FROM views", con = dbcon)
dbcon = lite.connect("C:/Users/Barrett/Documents/Delpro Files/DDMParlor.db")
test = pd.read_sql("SELECT name FROM sqlite_master WHERE type = 'table'",dbcon)
df = pd.read_sql_query("SELECT * FROM table_name", dbcon)
df = pd.read_sql_query("SELECT * FROM AnimalData", dbcon)
df = pd.read_sql_query("SELECT * FROM dbo.AbstractAnimalConfig", dbcon)
df = pd.read_sql_query("SELECT * FROM dbo.AnimalData", dbcon)
df = pd.read_sql("SELECT * FROM dbo.AnimalData", dbcon)
df = pd.read_sql("SELECT * FROM AnimalData", dbcon)
df = pd.read_sql("SELECT * FROM 'dbo.AnimalData'", dbcon)

## ---(Tue Jun 19 21:37:58 2018)---
import sqlite3 as lite
import pyodbc
import pandas as pd


conn = pyodbc.connect(r'Driver={SQL Server};Server=TE-DAIRY\DELPRO;Database=DDMParlor;Trusted_Connection=yes;')
dbcon = lite.connect("C:/Users/Barrett/Documents/Delpro Files/DDMParlor.db")
test2 = pd.read_sql("SELECT COLUMN_NAME, * FROM INFORMATION_SCHEMA.COLUMNS", dbcon)
test3 = pd.read_sql("SELECT COUNT(*) FROM rad.LuPrivilege", MRPA).iloc[0,0]
test2 = pd.read_sql("SELECT table_name [Table Name], column_name [Column Name] FROM information_schema.columns where data_type = 'NTEXT'", dbcon)
test2 = pd.read_sql("SELECT table_name [Table Name], column_name [Column Name] FROM information_schema.columns", dbcon)
test2 = pd.read_sql("SELECT table_name, column_name FROM information_schema.columns", dbcon)
dbcon.tables
dbcon.tables()
tablenames = []

for rows in cursor.tables():
    tablename = str(rows.table_schem)+"."+str(rows.table_name)
    tablenames.append(tablename)
    
cursor = dbcon.cursor()
tablenames = []

for rows in cursor.tables():
    tablename = str(rows.table_schem)+"."+str(rows.table_name)
    tablenames.append(tablename)
    
cursor.fetchall()
print(cursor.fetchall())
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
print(cursor.fetchall())
test2 = pd.read_sql("SELECT name FROM sqlite_master WHERE type='table'", dbcon)c
test2 = pd.read_sql("SELECT name FROM sqlite_master WHERE type='table'", dbcon)
test2 = pd.read_sql("SELECT name FROM sqlite_master", dbcon)
for iter in test2:
    print(iter)
    
for iter in test2.iloc[:,0]:
    print(iter)
    
for iter in test2.iloc[:,0]:
    x = "SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED SELECT TOP 500 COUNT(*) FROM " + iter
    test = pd.read_sql(x, dbcon)
    print(iter)
    
for iter in test2.iloc[:,0]:
    x = "SELECT TOP 500 COUNT(*) FROM " + iter
    test = pd.read_sql(x, dbcon)
    print(iter)
    
for iter in test2.iloc[:,0]:
    x = "SELECT COUNT(*) FROM " + iter
    test = pd.read_sql(x, dbcon)
    print(iter)
    
for iter in test2.iloc[:,0]:
    x = "SELECT COUNT(*) FROM '" + iter + "'"
    test = pd.read_sql(x, dbcon)
    print(iter)
    
Pragma table_info('sys.xml_schema_wildcards')
output = pd.DataFrame()
for iter in test2.iloc[:,0]:
    x = "SELECT COUNT(*) FROM '" + iter + "'"
    test = pd.read_sql(x, dbcon)
    output = output.append([])

    print(iter)
    
    
    
test['table'] = 0
for iter in test2.iloc[:,0]:
    x = "SELECT COUNT(*) FROM '" + iter + "'"
    test = pd.read_sql(x, dbcon)
    test['table'] = iter
    
for iter in test2.iloc[:,0]:
    x = "SELECT COUNT(*) FROM '" + iter + "'"
    test = pd.read_sql(x, dbcon)
    test['table'] = iter
    output = output.append(test,ignore_index = True)
    
output = output.sort_values(['COUNT(*)'])
output = output.sort_values(['COUNT(*)'], ascending = False)
output.to_excel('C:\/Users/Barrett/Documents/Delpro Files/DDMParlor Tables.xlsx, index=False)
output.to_excel('C:\/Users/Barrett/Documents/Delpro Files/DDMParlor Tables.xlsx', index=False)
dbcon = lite.connect("C:/Users/Barrett/Documents/Delpro Files/master.db")
test2 = pd.read_sql("SELECT name FROM sqlite_master", dbcon)

output = pd.DataFrame()
for iter in test2.iloc[:,0]:
    x = "SELECT COUNT(*) FROM '" + iter + "'"
    test = pd.read_sql(x, dbcon)
    test['table'] = iter
    output = output.append(test,ignore_index = True)
output = output.sort_values(['COUNT(*)'], ascending = False)

output.to_excel('C:/Users/Barrett/Documents/Delpro Files/master Tables.xlsx', index=False)


dbcon.close()
dbcon = lite.connect("C:/Users/Barrett/Documents/Delpro Files/model.db")
test2 = pd.read_sql("SELECT name FROM sqlite_master", dbcon)

output = pd.DataFrame()
for iter in test2.iloc[:,0]:
    x = "SELECT COUNT(*) FROM '" + iter + "'"
    test = pd.read_sql(x, dbcon)
    test['table'] = iter
    output = output.append(test,ignore_index = True)
output = output.sort_values(['COUNT(*)'], ascending = False)

output.to_excel('C:/Users/Barrett/Documents/Delpro Files/master Tables.xlsx', index=False)


dbcon = lite.connect("C:/Users/Barrett/Documents/Delpro Files/msdb.db")
test2 = pd.read_sql("SELECT name FROM sqlite_master", dbcon)

output = pd.DataFrame()
for iter in test2.iloc[:,0]:
    x = "SELECT COUNT(*) FROM '" + iter + "'"
    test = pd.read_sql(x, dbcon)
    test['table'] = iter
    output = output.append(test,ignore_index = True)
output = output.sort_values(['COUNT(*)'], ascending = False)

output.to_excel('C:/Users/Barrett/Documents/Delpro Files/master Tables.xlsx', index=False)



## ---(Fri May 31 18:14:56 2019)---
runfile('C:/Users/Barrett/.spyder-py3/DCtest.py', wdir='C:/Users/Barrett/.spyder-py3')

## ---(Sat Aug 24 08:22:04 2019)---
runfile('C:/Users/Barrett/.spyder-py3/Delpro Analysis.py', wdir='C:/Users/Barrett/.spyder-py3')
test2.loc[:,'DayDate'].min()
test2.loc[:,'DayDate'].max()
animalsummary = test2.loc[:,['Animal', 'DailyYield']]
animalsummary = animalsummary.groupby('Animal', as_index = False).Sum()
animalsummary = animalsummary.groupby('Animal', as_index = False).sum()
test3 = pd.read_sql('SELECT * FROM 'dbo.MilkingPerformanceMilkYield', dbcon)
test3 = pd.read_sql("SELECT * FROM 'dbo.MilkingPerformanceMilkYield'", dbcon)
test3.loc[:,'BeginTime'].max()
test3.loc[:,'BeginTime'].min()
col = ['AnimalOid', 'Slips', 'Blocks', 'KickOffs', 'AutoTakeOff', \
       'NoOfReattaches', 'ManualMode', 'ManualDetach', 'BlockOverride', \
       'TotalYield', 'ForcedRetract']

milkingdata = test3.loc[:, col]
milkingsummary = milkingdata.groupby('AnimalOid', as_index = False).sum()

## ---(Wed Aug 28 22:07:25 2019)---
for line in open("C:/Users/Barrett/Documents/DC Datafile/COWFILE1.DAT", 'r'):
    print(line.rstrip())

for line in 8:
open("C:/Users/Barrett/Documents/DC Datafile/COWFILE1.DAT", 'r')
for line in open("C:/Users/Barrett/Documents/DC Datafile/COWFILE1.DAT", 'r'):
    print(line.rstrip())
    print(line)

for line in open("C:/Users/Barrett/Documents/DC Datafile/COWFILE1.DAT", 'r', encoding='utf8'):
print(line)
runfile('C:/Users/Barrett/.spyder-py3/DCtest.py', wdir='C:/Users/Barrett/.spyder-py3')

## ---(Wed Aug 28 22:31:25 2019)---
open("C:/Users/Barrett/Documents/DC Datafile/COWFILE1.DAT", mode='r', encoding='Latin-1')
import chardet
rawdata = open("C:/Users/Barrett/Documents/DC Datafile/COWFILE1.DAT", mode='r', encoding='Latin-1')
rawdata = open("C:/Users/Barrett/Documents/DC Datafile/COWFILE1.DAT", mode='r')
rawdata = open("C:/Users/Barrett/Documents/DC Datafile/COWFILE1.DAT", mode='r').read()
chardet.detect(rawdata)
rawdata = open("C:/Users/Barrett/Documents/DC Datafile/COWFILE1.DAT", mode='r').read()

## ---(Mon Oct 14 11:56:17 2019)---
runfile('C:/Users/Barrett/.spyder-py3/Delpro Analysis.py', wdir='C:/Users/Barrett/.spyder-py3')
test2.loc[:,'DayDate'].max()
test2.loc[:,'DayDate'].min)
test2.loc[:,'DayDate'].min())
test2.loc[:,'DayDate'].min()
daily = pd.read_sql("SELECT * FROM 'dbo.AnimalDaily'", dbcon)
daily.loc[:,'Date'].max()
daily.loc[:,'Date'].min()
daily.loc[:,'Date'].max()
daily.loc[:,'Date'].min()
daily.loc[:,'BasicAnimal'].max()
daily.loc[:,'BasicAnimal'].min()
daily2 = daily[daily.Date >= '01/01/2019']
dairy2.info()
daily2.info()
daily.iloc[0,1]
import datetime
daily['Date'] = daily.apply(lambda row: datetime.datetime.strptime(row['Date'],"%Y-%m-%d"))
daily['Date'] = daily.apply(lambda row: datetime.datetime.strptime(row['Date'],"%Y-%m-%d"), axis=1)
daily.info()
daily.loc[:,'Date'].max()
daily.loc[:,'Date'].min()
daily.loc[:,'Date'].min().year
daily['Year'] = daily.apply(lambda row: row['Date'].year, axis = 1)
groupdaily = daily.groupby(by='Year',as_index=False).count()
test2.info()
test2.iloc[0,:]
test2.iloc[-1,:]
test2['DayDate'] = test2.apply(lambda row: datetime.datetime.strptime(row['DayDate'],"%Y-%m-%d %h:%m:%s"), axis=1)
test2['Year'] = test2.apply(lambda row: row['DayDate'].year, axis = 1)
grouphistory = test2.groupby(by='Year',as_index=False).count()
test2['DayDate'] = test2.apply(lambda row: datetime.datetime.strptime(row['DayDate'],"%Y-%m-%d %H:%m:%s"), axis=1)
test2['DayDate'] = test2.apply(lambda row: datetime.datetime.strptime(row['DayDate'],"%Y-%m-%d %H:%M:%S"), axis=1)
milkingdata = pd.read_sql("SELECT * FROM 'dbo.MilkingPerformanceMilkYield'", dbcon)
test2['Year'] = test2.apply(lambda row: row['DayDate'].year, axis = 1)
grouphistory = test2.groupby(by='Year',as_index=False).count()
milkingdata.info()
milkingdata.iloc[0,:]
milkingdata['Date'] = milkingdata.apply(lambda row: datetime.datetime.strptime(row['BeignTime'],"%Y-%m-%d %H:%M:%S"), axis=1)
milkingdata['Date'] = milkingdata.apply(lambda row: datetime.datetime.strptime(row['EndTime'],"%Y-%m-%d %H:%M:%S"), axis=1)
milkingdata['Date'] = milkingdata.apply(lambda row: datetime.datetime.strptime(row['BeginnTime'],"%Y-%m-%d %H:%M:%S"), axis=1)
milkingdata['Date'] = milkingdata.apply(lambda row: datetime.datetime.strptime(row['EndTime'],"%Y-%m-%d %H:%M:%S"), axis=1)
milkingdata['BeginTime'] = milkingdata.apply(lambda row: datetime.datetime.strptime(row['BeginTime'],"%Y-%m-%d %H:%M:%S"), axis=1)
milkingdata['EndTime'] = milkingdata.apply(lambda row: datetime.datetime.strptime(row['EndTime'],"%Y-%m-%d %H:%M:%S"), axis=1)
milkingdata.iloc[627,:]
milkingdata['EndTime'] = milkingdata.apply(lambda row: datetime.datetime.strptime(row['EndTime'],"%Y-%m-%d %H:%M:%S.%f"), axis=1)
milkingdata.iloc[0,8]
milkingdata.iloc[0,7]
len(milkingdata.iloc[0,7])
len(milkingdata.iloc[627,7])
left(milkingdata.iloc[627,7],19)
milkingdata.iloc[627,7][-19]
milkingdata.iloc[627,7][:19]
milkingdata['BeginTime'] = milkingdata['BeginTime'][:19]
milkingdata['EndTime'] = milkingdata['EndTime'][:19]
milkingdata['BeginTime'] = milkingdata.apply(lambda row: datetime.datetime.strptime(row['BeginTime'],"%Y-%m-%d %H:%M:%S"), axis=1)
milkingdata['EndTime'] = milkingdata.apply(lambda row: datetime.datetime.strptime(row['EndTime'],"%Y-%m-%d %H:%M:%S.%f"), axis=1)
milkingdata = pd.read_sql("SELECT * FROM 'dbo.MilkingPerformanceMilkYield'", dbcon)
milkingdata.iloc[0,7]
milkingdata.iloc[0,7].year
milkingdata.iloc[500,7].year
milkingdata['BeginDate'] = pd.to_datetime(milkingdata['BeginTime'], errors='coerce')
milkingdata.iloc[0,26].year
milkingdata['BeginTime'] = pd.to_datetime(milkingdata['BeginTime'], errors='coerce')
milkingdata['EndTime'] = pd.to_datetime(milkingdata['EndTime'], errors='coerce')
milkingdata['Year'] = milkingdata.apply(lambda row: row['BeginTime'].year, axis=1)
EndTime
milkingdata['Year'] = milkingdata.apply(lambda row: row['BeginTime'].year, axis=1)
milkingdata.groupby(by='Year').count()
milksummary = milkingdata.groupby(by='Year', as_index=False).count()

## ---(Tue Oct 22 23:23:03 2019)---
import numpy as np
myarray = np.fromfile('C:/Users/Barrett/Documents/DC Datafile/COWFILE1.DAT', dtype=float)
myarray = np.fromfile('C:/DC/COWFILE1.DAT', dtype=float)
myarray = np.fromfile('C:/DC/COWFILE1.DAT', dtype=np.uint8)

## ---(Wed Oct 23 20:08:36 2019)---
import os
import sys

path = os.path.dirname('C:/Program Files (x86)/FoersterTechnik/KM3/')

file_name = 'DSPKM.FDB'
if __name__ == "__main__":
    with open(os.path.join(path, './' + file_name), 'r', encoding='cp1252') as f1:
        lines = f1.read()
        f2 = open(os.path.join(path, './' + 'my_output_file.xml'), 'w', encoding='utf-8')
        f2.write(lines)
        f2.close()

if __name__ == "__main__":
    with open(os.path.join(path, './' + file_name), 'r', encoding='cp1252') as f1:
        try:
            lines = f1.read()
            f2 = open(os.path.join(path, './' + 'my_output_file.xml'), 'w', encoding='utf-8')
            f2.write(lines)
            f2.close()
        except:
            print("Did not work")

for line in open("C:/Program Files (x86)/FoersterTechnik/KM3/DSPKM.FDB", mode='r', encoding='Latin-1'):
    print(line.rstrip())

import poster
import FDB
import fdb
import fdb
conn = fdb.connect(dsn='JA:E:\New folder\FoersterTechnik\KM3\DSPKM.FDB', user='sysdba',password='C15B8BB945E628A441F1') 


import fdb
import fbd

## ---(Wed Oct 23 20:40:55 2019)---
import fdb
conn = fdb.connect(dsn='JA:E:\New folder\FoersterTechnik\KM3\DSPKM.FDB', user='sysdba',password='C15B8BB945E628A441F1') 
conn = fdb.connect(host='JA', database=':E:\New folder\FoersterTechnik\KM3\DSPKM.FDB', user='sysdba',password='C15B8BB945E628A441F1') 
conn = fdb.connect(host='JA', database=':E:\New folder\FoersterTechnik\KM3\DSPKM.FDB', user='sysdba', password='C15B8BB945E628A441F1') 
conn = fdb.connect(host='JA', database='E:\New folder\FoersterTechnik\KM3\DSPKM.FDB', user='sysdba', password='C15B8BB945E628A441F1') 
conn = fdb.connect(host='JA', database='E:\New folder\FoersterTechnik\KM3\DSPKM.FDB', user='sysdba', password='C15B8BB945E628A441F1') 
conn = fdb.connect(database='E:\New folder\FoersterTechnik\KM3\DSPKM.FDB', user='sysdba', password='C15B8BB945E628A441F1') 
conn = fdb.connect(dsn='E:\New folder\FoersterTechnik\KM3\DSPKM.FDB', user='sysdba', password='C15B8BB945E628A441F1') 
conn = fdb.connect(host='JA', dsn='E:\New folder\FoersterTechnik\KM3\DSPKM.FDB', user='sysdba', password='C15B8BB945E628A441F1') 
conn = fdb.connect(host='JA', server="127.0.0.1", dsn='E:\New folder\FoersterTechnik\KM3\DSPKM.FDB', user='sysdba', password='7A93C3708FB85AF213C7', charset='windows-1252') 
conn = fdb.connect(server="127.0.0.1", database='E:\New folder\FoersterTechnik\KM3\DSPKM.FDB', user='sysdba', password='7A93C3708FB85AF213C7', charset='windows-1252') 
conn = fdb.connect(database='E:\New folder\FoersterTechnik\KM3\DSPKM.FDB', user='sysdba', password='7A93C3708FB85AF213C7', charset='windows-1252') 
conn = fdb.connect(database='E:\New folder\FoersterTechnik\KM3\DSPKM.FDB', user='sysdba', password='7A93C3708FB85AF213C7', charset='1252') 
conn = fdb.connect(database='E:\New folder\FoersterTechnik\KM3\DSPKM.FDB', user='sysdba', password='C15B8BB945E628A441F1') 
chdir('C:/Program Files (x86)/FoersterTechnik/KM3)
chdir('C:/Program Files (x86)/FoersterTechnik/KM3')
conn = fdb.connect(database='E:/New folder/FoersterTechnik/KM3/DSPKM.FDB', user='sysdba', password='C15B8BB945E628A441F1') 
conn = fdb.connect(database='C:/Program Files (x86)/FoersterTechnik/KM3/DSPKM.FDB', user='sysdba', password='C15B8BB945E628A441F1') 
conn = fdb.connect(database="C:/Program Files (x86)/FoersterTechnik/KM3/DSPKM.FDB", user='sysdba', password='C15B8BB945E628A441F1') 
os.chdir('C:/Program Files (x86)/FoersterTechnik/KM3')
import os
os.chdir('C:/Program Files (x86)/FoersterTechnik/KM3')
conn = fdb.connect(database="DSPKM.FDB", user='sysdba', password='C15B8BB945E628A441F1') 
conn = fdb.connect(database="dspKM.fdb", user='sysdba', password='C15B8BB945E628A441F1') 
conn = fdb.connect(database='C:/Program Files/Firebird/Firebird_3_0/examples/empbuild/EMPLOYEE.FDB')
os.chdir('C:/Program Files/Firebird/Firebird_3_0/examples/empbuild/')
conn = fdb.connect(database='C:/Program Files/Firebird/Firebird_3_0/examples/empbuild/EMPLOYEE.FDB')
os.chdir('C:/')
conn = fdb.connect(database='C:/TEST.FDB')
conn = fdb.connect(database='TEST.FDB')
conn = fdb.connect(database='TEST.FDB', user='sysdba', password='masterkey')
conn = fdb.connect(dsn='C:/TEST.fdb', user='SYSDBA', password='masterkey')
conn = fdb.connect(database='C:/TEST.fdb', user='SYSDBA', password='masterkey')
conn = fdb.connect(database="dspKM.fdb", user='sysdba', password='masterkey')
tablelist = ['DSP$UPDATE', 'KM_BGRUPPE', 'KM_DRUCK', 'KM_KALB', 'KM_KF_TERMIN',
             'KM_SENDER', 'KM_STAMM', 'KM_TA_ZUBEHOER', 'KM_TRAENKE', 
             'KM_TRAENKE_TERMIN', 'KM_ANSICHT', 'KM_BGRUPPE_KALB,
             'KM_HASH', 'KM_KF_ALARM', 'KM_PLAN', 'KM_SILO', 'KM_TA'
             , 'KM_TEMERATUR', 'KM_TRAENKE_ALARM', 'KM_VERZEHR']
tablelist = ['DSP$UPDATE', 'KM_BGRUPPE', 'KM_DRUCK', 'KM_KALB', 'KM_KF_TERMIN',
             'KM_SENDER', 'KM_STAMM', 'KM_TA_ZUBEHOER', 'KM_TRAENKE', 
             'KM_TRAENKE_TERMIN', 'KM_ANSICHT', 'KM_BGRUPPE_KALB',
             'KM_HASH', 'KM_KF_ALARM', 'KM_PLAN', 'KM_SILO', 'KM_TA'
             , 'KM_TEMERATUR', 'KM_TRAENKE_ALARM', 'KM_VERZEHR']

## ---(Fri Jan 10 20:07:43 2020)---
dbcon = lite.connect("C:/km3.db")
import sqlite3 as lite
dbcon = lite.connect("C:/km3.db")
x = pd.DateFrame(['Test', 'table'])
x
x = pd.DateFrame([['Test', 'table']])
x
x.to_sql(test, dbcon, if_exists = 'append', index = False)
dbcon2 = lite.connect("C:/Users/Barrett/Documents/Delpro Files/DDMParlor2.db")
test2 = pd.read_sql("SELECT * FROM 'dbo.HistoryAnimalDailyData'", dbcon)
test2 = pd.read_sql("SELECT * FROM 'dbo.HistoryAnimalDailyData'", dbcon2)
test2
test2.head()
x=1
import pandas as pd
import sqlite3 as lite
import pyodbc
import datetime

dbcon = lite.connect("C:/Users/Barrett/Documents/km3.db")

datadb = pd.read_sql("SELECT kb.ID, kb.NUMMER as 'Tag', \
                     tr.* \
                     FROM KM_TRAENKE as tr LEFT JOIN \
                     KM_KALB as kb \
                     ON kb.ID = tr.KALB",
                     dbcon)
import pandas as pd
import sqlite3 as lite
import pyodbc
import datetime

dbcon = lite.connect("C:/Users/Barrett/Documents/km3.db")

datadb = pd.read_sql("SELECT kb.ID, kb.NUMMER as 'Tag', \
                     tr.* \
                     FROM KM_TRAENKE as tr LEFT JOIN \
                     KM_KALB as kb \
                     ON kb.ID = tr.KALB",
                     dbcon)
x = datadb.head(500)
x
x.head()
datadb.head()

## ---(Fri Jan 10 22:26:50 2020)---
import pandas as pd
import sqlite3 as lite
import pyodbc
import datetime

dbcon = lite.connect("C:/Users/Barrett/Documents/km3.db")

datadb = pd.read_sql("SELECT kb.ID, kb.NUMMER as 'Tag', \
                     tr.* \
                     FROM KM_TRAENKE as tr LEFT JOIN \
                     KM_KALB as kb \
                     ON kb.ID = tr.KALB",
                     dbcon)
datadb.head()
test = datadb.head(500)
test = datadb[datadb.Tag == 4556]
test = datadb[datadb.Tag == 8008]
test.columns
test = datadb[datadb.Tag == 4556]
group = datadb.loc[:, ['Tag', 'SOLL', 'SOLL_RM', 'ABRUF',
                       'BESUCH_OT', 'BESUCH_MT']]
group = group.groupby(by = 'Tag').sum()
group = datadb.loc[:, ['Tag', 'SOLL', 'SOLL_RM', 'ABRUF',
                       'BESUCH_OT', 'BESUCH_MT']]
group.head()
group = group.groupby(by = 'Tag', axis=1).sum()
groupx = group.groupby(by = 'Tag').sum()
group = datadb.loc[:, ['Tag', 'SOLL', 'SOLL_RM', 'ABRUF',
                       'BESUCH_OT', 'BESUCH_MT']]
groupx = group.groupby(by = 'Tag').sum()
groupx = group.groupby(by = 'Tag', as_index = False).sum()
groupx.loc[:, 'BESUCH_OT'].max()
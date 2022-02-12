# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 08:22:52 2019

@author: Barrett
"""

import sqlite3 as lite
import pyodbc
import pandas as pd
import datetime

kgtolbs = 2.20462262

dbcon = lite.connect("C:/Users/Barrett/Documents/Delpro Files/DDMParlor2.db")

test2 = pd.read_sql("SELECT * FROM 'dbo.HistoryAnimalDailyData'", dbcon)
daily = pd.read_sql("SELECT * FROM 'dbo.AnimalDaily'", dbcon)
milkingdata = pd.read_sql("SELECT * FROM 'dbo.MilkingPerformanceMilkYield'", dbcon)

milkingdata['BeginTime'] = pd.to_datetime(milkingdata['BeginTime'], errors='coerce')
milkingdata['EndTime'] = pd.to_datetime(milkingdata['EndTime'], errors='coerce')
milkingdata['Year'] = milkingdata.apply(lambda row: row['BeginTime'].year, axis=1)
milksummary = milkingdata.groupby(by='Year', as_index=False).count()
#milkingdata['BeginTime'] = milkingdata['BeginTime'][:19]
#milkingdata['EndTime'] = milkingdata['EndTime'][:19]
#milkingdata['BeginTime'] = milkingdata.apply(lambda row: datetime.datetime.strptime(row['BeginTime'],"%Y-%m-%d %H:%M:%S"), axis=1)
#milkingdata['EndTime'] = milkingdata.apply(lambda row: datetime.datetime.strptime(row['EndTime'],"%Y-%m-%d %H:%M:%S.%f"), axis=1)



daily['Date'] = daily.apply(lambda row: datetime.datetime.strptime(row['Date'],"%Y-%m-%d"), axis=1)
daily['Year'] = daily.apply(lambda row: row['Date'].year, axis = 1)
groupdaily = daily.groupby(by='Year',as_index=False).count()

test2['DayDate'] = test2.apply(lambda row: datetime.datetime.strptime(row['DayDate'],"%Y-%m-%d %H:%M:%S"), axis=1)
test2['Year'] = test2.apply(lambda row: row['DayDate'].year, axis = 1)
grouphistory = test2.groupby(by='Year',as_index=False).count()

daily.loc[:,'Date'].max()
daily.loc[:,'Date'].min()
daily.loc[:,'BasicAnimal'].min()
test2.loc[:,'DayDate'].max()
test2.loc[:,'DayDate'].min()


test2['MilkYieldLBS'] = test.apply(lambda row: row['Yiel])

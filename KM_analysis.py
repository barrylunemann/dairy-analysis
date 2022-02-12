# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 22:04:55 2020

@author: Barrett
"""

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

test = datadb[datadb.Tag == 8008]

germandict = {'KALB' : 'Calf',
              'SOLL' : 'Should', #target
              'SOLL_RM' : 'Should_RM',
              'ABRUF' : 'Call', #Possibly actual amt drank?
              'ABRUF_PR' : 'Call_PR',
              'SAUG' : 'Suction',
              'SAUG_PR' : 'Suction_PR',
              'ABBR_OZ' : 'Cancellation without addition',
              'ABBR_MZ' : 'Cancellation with addition',
              'BESUCH_OT' : 'Visit_OT', #Visit Without Drinking
              'BESUCH_MT' : 'Visit_MT', #Visit With Drinking
              'GEWICHT' : 'Weight',
              'GEWICHT_AENDERUNG' : 'Change'}

group = datadb.loc[:, ['Tag', 'SOLL', 'SOLL_RM', 'ABRUF',
                       'BESUCH_OT', 'BESUCH_MT']]
groupx = group.groupby(by = 'Tag', as_index = False).sum()


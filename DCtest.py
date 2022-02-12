# -*- coding: utf-8 -*-
"""
Created on Fri May 31 18:15:07 2019

@author: Barrett
"""

import numpy as np
myarray = np.fromfile('C:/DC/COWFILE1.DAT', dtype=np.uint8)


import fdb
conn = fdb.connect(dsn='JA:E:\New folder\FoersterTechnik\KM3\DSPKM.FDB', user='sysdba',password='C15B8BB945E628A441F1') 




from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
import urllib2

# Register the streaming http handlers with urllib2
register_openers()

# Use multipart encoding for the input files
datagen, headers = multipart_encode({ 'files[]': open('example.fdb/gdb', 'rb')})

# Create the request object
request = urllib2.Request('https://www.rebasedata.com/api/v1/convert', datagen, headers)

# Do the request and get the response
# Here the Firebird file gets converted to CSV
response = urllib2.urlopen(request)

# Check if an error came back
if response.info().getheader('Content-Type') == 'application/json':
    print response.read()
    sys.exit(1)

# Write the response to /tmp/output.zip
with open('/tmp/output.zip', 'wb') as local_file:
    local_file.write(response.read())

print 'Conversion result successfully written to /tmp/output.zip!'





for line in open("C:/Program Files (x86)/FoersterTechnik/KM3/DSPKM.FDB", mode='r', encoding='Latin-1'):
    print(line.rstrip())
    #print(line)


import os
import sys

path = os.path.dirname('C:/Program Files (x86)/FoersterTechnik/KM3/')

file_name = 'DSPKM.FDB'

if __name__ == "__main__":
    with open(os.path.join(path, './' + file_name), 'r', encoding='cp1252') as f1:
        
        
        try:
            lines = f1.read()
            f2 = open(os.path.join(path, './' + 'my_output_file.xml'), 'w', encoding='utf-8')
            f2.write(lines)
            f2.close()
        except:
            print("Did not work")




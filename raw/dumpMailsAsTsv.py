#! /usr/bin/python
import couchdb
import sys
import os
import csv
import json
import io

from uuid import uuid4

dirname = os.path.dirname
abspath = os.path.abspath

dirName = sys.argv[1]
dbName = sys.argv[2]
rawDataPath = os.path.join(dirname(dirname(dirname(abspath(__file__)))),
                           "data","raw","enron_mail_20110402","maildir" )
procDataPath = os.path.join(dirname(dirname(dirname(abspath(__file__)))),
                            "data","proc")
scanDir = os.path.join(rawDataPath,dirName)
dumpDir = os.path.join(procDataPath,dirName)

server = couchdb.Server('http://127.0.0.1:5984/')
db = server[dbName]

def parseMail(file):
    bodyFlag = False
    jsonDB = {}
    for line in file:
        if bodyFlag:
            jsonDB['body'] = []
            value[0] = 'body'
        if(line.find(":") != -1 and not bodyFlag):
            value = line.rstrip('\n').rstrip('\r').split(":", 2)
            try:
                jsonDB[value[0]]
            except KeyError:
                jsonDB[value[0]] = [value[1]]
                            
        elif line.rstrip('\n').rstrip('\r'):
            jsonDB[value[0]].append(line.rstrip('\n').rstrip('\r'))
        else:
            bodyFlag = True
    #print "\n",json.dumps(jsonDB)        
    doc_id = uuid4().hex
    db[doc_id] = jsonDB
    

def  processDir(dir):
    print "processing ",dir
    dumpstr = []
    for file in os.listdir(dir):
        if(os.path.isdir(os.path.join(dir, file))):
               processDir(os.path.join(dir, file))
        else:
            fp = io.open(os.path.join(dir, file), 
                         mode='U', newline = '')
            parseMail(fp)
    


if (not(os.path.isdir(scanDir))): 
    exit
print "Dumping all files in :", scanDir, " into the couchDB instance\n"

for root, dirs, files in os.walk(scanDir):
    for dir in dirs:
        if not os.path.isdir(os.path.join(scanDir, dir)):
            continue
        if dir == 'inbox' : processDir(os.path.join(scanDir, dir))

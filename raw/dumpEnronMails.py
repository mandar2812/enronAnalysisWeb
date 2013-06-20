#! /usr/bin/python
import sys
import os
import io
dbName = sys.argv[1]
dirname = os.path.dirname
abspath = os.path.abspath

rawDataPath = os.path.join(dirname(dirname(dirname(abspath(__file__)))),
                           "data","raw","enron_mail_20110402","maildir" )
procDataPath = os.path.join(dirname(dirname(dirname(abspath(__file__)))),
                            "data","proc")

if (not(os.path.isdir(rawDataPath))): 
    exit
for root, dirs, files in os.walk(rawDataPath):
    for dir in dirs:
        if not os.path.isdir(os.path.join(rawDataPath, dir)):
            continue
        print "\n**************************************************"
        command = "./userMailsToCouchDB.py "+dir+" "+dbName
        print "\n",command,"\n"
        os.system(command)

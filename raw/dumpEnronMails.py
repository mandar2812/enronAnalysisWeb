#! /usr/bin/python
'''
Author: Mandar Chandorkar
Project : Enron

This script takes the directory name of a folder inside the enron mails
and runs the script userMailsToCouchDB.py to dump all the mails of that
directory(or mails of one person) into the CouchDB instance.
'''
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

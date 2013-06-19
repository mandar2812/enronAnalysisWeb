#! /usr/bin/python
import couchdb
import sys
import os
from uuid import uuid4
fields = ["Message-ID", "Date", "From", "To", 
          "Subject", "CC","Mime-Version", 
          "Content-Type", "Content-Transfer-Encoding", 
          "X-From", "X-To", "X-cc", "X-bcc", 
          "X-Folder", "X-Origin", "X-FileName", "body"]

server = couchdb.Server('http://127.0.0.1:5984/')
db = server['enron_mail_fields']
for field in fields:
    if field in db:
        print "\n",field," is already in ",db.name
    else:
        db[field] = {'type': 'attribute'}
    

print "\nDumping names of fields ...\n"
for doc in db:
    print db[doc],"\n"


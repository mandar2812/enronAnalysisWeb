#! /usr/bin/python
import sys
import random
import json
import os
import couchdb
lim = sys.argv[1]
dirname = os.path.dirname
abspath = os.path.abspath
server = couchdb.Server('http://127.0.0.1:5984/')
db = server['enron_email_dump']

os.chdir("../../data/proc")
dumpFile = "enron_mails_inbox.json"
fp = open(dumpFile, 'w')
num = random.randint(int(lim), int(2*lim))
samplelist = random.sample(db, int(lim))
filename = "email_dump_"+str(num)+".json"
fp = open(filename, 'w')
for doc_id in samplelist:
    json.dump(db[doc_id], fp, sort_keys = True, indent = 0)

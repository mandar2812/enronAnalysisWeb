#! /usr/bin/python
'''
Author : Mandar Chandorkar
Project : Enron Data Set Experiments

This script takes two arguments, 
lim(sampling limit) and dumpFileName
(file to dump graph data in) and outputs 
a csv file separated by pipes, into the 
$PROJECT_HOME/data/proc directory containing
the graph linkages of the sampled mails, their nodes
and their edge strengths

Rules for determining edge strength are as follows :

1) To (Direct Mail):- 0.5/number of recipients
2) CC (Copied in Mail):- 0.4/number of recipients
3) BCC (Copied in secret):- 0.1/number of recipients

Files are dumped in the following format
MessageID|DateTime|From|To|EdgeStrength
4fggfgggg|Mon, 22 Oct 2001 11|John Doe|Mary Doe|0.5
   
'''
import sys
import random
import os
import couchdb
import re
lim = sys.argv[1]
dumpFileName = sys.argv[2]
namesRegExp = ' (\w+,\s\w+) <([^><]+)>,?'
baseStrength = {'To' : 1, 'CC':0.05, 'BCC':0.04}

dirname = os.path.dirname
abspath = os.path.abspath

server = couchdb.Server('http://127.0.0.1:5984/')
db = server['enron_email_dump']

os.chdir("../../data/proc")

num = random.randint(int(lim), int(2*lim))
samplelist = random.sample(db, int(lim))

import time
import datetime
import csv
with open(dumpFileName, 'wb') as csvfile:
    graphwriter = csv.writer(csvfile, delimiter='|',
                             quotechar='"', quoting=csv.QUOTE_MINIMAL)
    graphwriter.writerow(['MessageID', 'TimeStamp', 'From', 'To', 'EdgeStrength'])
    for doc_id in samplelist:
        match = {}
        doc = db[doc_id]
        dateMat = re.search('\[\'(.+)\'\]', str(doc['Date']))
        dateStr = dateMat.group(1).strip()
        timest = int(time.mktime(
            datetime.datetime.strptime(dateStr, "%a, %d %b %Y %H").
            timetuple()) + 48600)
        matchFrom = re.findall(namesRegExp, str(doc['X-From']))
        match['To'] = re.findall(namesRegExp, str(doc['X-To']))
        match['CC'] = re.findall(namesRegExp, str(doc['X-cc']))
        match['BCC'] = re.findall(namesRegExp, str(doc['X-bcc']))
        for i in match:
            numPeople = len(match[i])
            if numPeople > 0 and matchFrom:
                for j in match[i]:
                    graphwriter.writerow([str(doc['_id']), timest, 
                                          matchFrom[0][0].replace(',', ''), 
                                          j[0].replace(',', ''), 
                                          baseStrength[i]])
         

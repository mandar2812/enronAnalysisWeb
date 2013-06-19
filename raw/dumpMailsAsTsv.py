#! /usr/bin/python
import sys
import os
import csv

dirname = os.path.dirname
abspath = os.path.abspath
fields = ["Message-ID", "Date", "From", "To", 
          "Subject", "CC","Mime-Version", 
          "Content-Type", "Content-Transfer-Encoding", 
          "X-From", "X-To", "X-cc", "X-bcc", 
          "X-Folder", "X-Origin", "X-FileName", "body"]

dirName = sys.argv[1]

rawDataPath = os.path.join(dirname(dirname(dirname(abspath(__file__)))),
                           "data","raw","enron_mail_20110402","maildir" )
procDataPath = os.path.join(dirname(dirname(dirname(abspath(__file__)))),
                            "data","proc")
scanDir = os.path.join(rawDataPath,dirName)
dumpDir = os.path.join(procDataPath,dirName)


def parseMail(file):
    fieldflags = {"Message-ID":0, "Date":0, "From":0, "To":0, 
                  "Subject":0, "Cc":0, "Mime-Version":0, "Content-Type":0, 
                  "Content-Transfer-Encoding":0, "Bcc":0,"X-From":0, 
                  "X-To":0, "X-cc":0, "X-bcc":0, "X-Folder":0, 
                  "X-Origin":0, "X-FileName":0, "body":0}
    linestr = []
    for line in file:
        value = line.rstrip().split(":", 2)
        if(line.find(":") == 1):
            value = line.rstrip().split(":", 2)
            linestr.append(value[1]) 
        else:
            linestr.append(line.rstrip())
    
    return linestr

def  processDir(dir):
    print "processing ",dir
    dumpstr = []
    for file in os.listdir(dir):
        if(os.path.isdir(os.path.join(dir, file))):
               dumpstr.append(processDir(os.path.join(dir, file)))
        else:
            fp = open(os.path.join(dir, file), 'U')
            dumpstr.append(parseMail(fp))
    return dumpstr

if (not(os.path.isdir(scanDir))): 
    exit
print "Dumping all files in :", scanDir, "as TSV files\n"

for root, dirs, files in os.walk(scanDir):
    for dir in dirs:
        if not os.path.isdir(os.path.join(scanDir, dir)):
            continue
        dumpstr = processDir(os.path.join(scanDir, dir))
        if not os.path.isdir(dumpDir):
            os.mkdir(dumpDir)
        dumN = dirName + "_" + dir + ".tsv"
        fw = open(os.path.join(dumpDir,dumN), "w")
        new_file = csv.DictWriter(fw, fieldnames = fields, delimiter='\t')
        new_file.writerows(dumpstr)

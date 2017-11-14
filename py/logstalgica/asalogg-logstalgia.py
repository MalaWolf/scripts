#!/usr/bin/env python
# Written By: Patrick Taylor
#*******Purpose Take iptables log and make it look like apache so we could use it with
#logstalgia
#**************** import modules here
import os
import sys
import re
import datetime
import sys # in case we decide to use STDIN instead to read logs
import time
from datetime import date

def tail_f(file):
        interval = 0.1
        while True:
                where = file.tell()
                line = file.readline()

                if not line:
                        time.sleep(interval)
                        file.seek(where)
                else:
                        yield line
#log file monitored
#print len(sys.argv)

if len(sys.argv) >= 2:
        file = sys.argv[1]
        f = open(file, 'r')
        FILESOURCE = f.readlines()
        FILEGIVEN = 1
else:
        FILESOURCE = sys.stdin.read
        FILEGIVEN = 0
#print FILEGIVEN
#quit

FILEDEST = "./asa-logstalgia.log"
#get year to properly format for logstalgia
now = datetime.datetime.now()
#print now
#quit
#begin work
def main():
    #while True:
     for message in tail_f(open(sys.argv[1])):
                messageSplit = message.split()
                #print messageSplit
                #print messageSplit[8]
                #print type(messageSplit)
                #break
                if messageSplit[6] == 'Deny' and  messageSplit[7] == 'tcp' or  messageSplit[7] == 'udp':
                        #get source ip
                        getSRC = messageSplit[9].split("/")[0].split(":")[1]
                        #SOURCE = re.search(r'\d+\.\d+\.\d+\.\d+',messageSplit[8].split("/")[0].split(":")[1])
                        #getSRC = SOURCE.group()
                        #get PROTOCOL
                        PROTO = re.search(r'\w+$',"udp53")
                        getPROTO = PROTO.group()
			#print  messageSplit[7]
			#if messageSplit[7] == 'icmp':
			#	#get ICMP type
			#	PORT="type_8"
                        	#get PORT
                        PORT = re.search(r'\d+$',messageSplit[9].split("/")[1])
                        getPORT = PORT.group()
				
                        #get destination ip
                        DESTINATION = re.search(r'\d+\.\d+\.\d+\.\d+',messageSplit[11].split(":")[1].split("/")[0])
                        getDST = DESTINATION.group()
                        # Strukturerer Query
                        QUERY=messageSplit[11]
                        # set STATUS lik type query
                        STATUS=messageSplit[6] 
                        #create list here to make proper date format
                        makeDateList = []
                        #for dateitem in messageSplit[0].split("-"):
                        #        makeDateList.append(dateitem)
			YEAR =str(date.today().year)
                        DATER = messageSplit[1] + "/" + messageSplit[0] + "/" + YEAR + ":" +  messageSplit[2]
                        text2Output = '''%s - - [%s +0200] "GET %s HTTP/1.0" %s - "-" "%s''' % (getSRC , DATER, QUERY, STATUS, getDST)
                        text2File = '''%s - - [%s +0200] "GET %s HTTP/1.0" %s - "-" "%s \n''' % (getSRC , DATER, QUERY, STATUS, getDST)
                        #fs = open(FILEDEST, 'a')
                        #fs.write(text2File)
                        print text2Output
                        #break
                        if FILEGIVEN == 1 :
                                f.close()
# 195.254.173.20 - - [05/Jun/2013:19:20:17 +0200] "GET 10.152.102.10.in-addr.arpa HTTP/1.0" IN_PTR - "-" "195.254.173.100

#run the following functions when script is called by name
if __name__ == '__main__':
        for line in tail_f(open(sys.argv[1])):
                main()

# 0  = 'Jun', 		1 = '11' 
# 2  = '07:26:21', 	3 = 'bp-ekstern', 
# 4  = ':', 		5 = '%ASA-4-106023:', 
# 6  = 'Deny', 		7 = 'tcp', 
# 8  = 'src', 		9 = 'outside:74.217.148.72/11576', 
# 10 = 'dst', 		11 ='DH-AC-DMZ:195.254.173.184/443', 
# 12 = 'by', 		13 = 'access-group', 
# 14 = '"outside_in"', 	15 = '[0x4cc7a6a3,', 
# 16= '0x0


#!/usr/bin/env python
# 
#Based on idea by: Patrick Taylor 
#*******Purpose:
# Take bind9 query log and make it look like apache so we could use it with logstalgia 
#**************** import modules here
import os 
import sys 
import re 
import datetime 
import sys # in case we decide to use STDIN instead to read logs

#log file monitored
#print len(sys.argv)

if len(sys.argv) >= 2:
	FILESOURCE = sys.argv[1]
	FILEGIVEN = 1 
else:
	FILESOURCE = sys.stdin
	FILEGIVEN = 0 

FILEDEST = "/var/log/bind9-logstalgia.log"
#get year to properly format for logstalgia
now = datetime.datetime.now()
#begin work
def main():
    #while True:
     for message in sys.stdin:
        	messageSplit = message.split()
		#print messageSplit 
		#print messageSplit[8] 
		#print type(messageSplit) 
		#break
        	if messageSplit[4] == 'query:':
            		#get source ip
            		SOURCE = re.search(r'(\d+\.\d+\.\d+\.\d+)',messageSplit[3].split("#")[0])
            		getSRC = SOURCE.group()
            		#get PROTOCOL
            		PROTO = re.search(r'\w+$',"udp53")
            		getPROTO = PROTO.group()
            		#get PORT
            		PORT = re.search(r'\d+$',messageSplit[3].split("#")[1].split(":")[0])
            		getPORT = PORT.group()
            		#get destination ip
            		DESTINATION = re.search(r'(\d+\.\d+\.\d+\.\d+)',messageSplit[9])
            		getDST = DESTINATION.group()
	    		# Strukturerer Query
	    		QUERY=messageSplit[5] 
	    		# set STATUS lik type query 
            		STATUS=messageSplit[6] + "_" + messageSplit[7]
            		#create list here to make proper date format
            		makeDateList = []
	    		for dateitem in messageSplit[0].split("-"):
            			makeDateList.append(dateitem)
            		DATER = '/'.join(makeDateList)+":"+messageSplit[1].split(".")[0]
            		text2Output = '''%s - - [%s +0200] "GET %s HTTP/1.0" %s - "-" "%s''' % (getSRC , DATER, QUERY, STATUS, getDST)
            		#fs = open(FILEDEST, 'a')
            		#fs.write(text2Output)
            		print text2Output
        		#break
            		if FILEGIVEN == 1 :
				f.close()

#run the following functions when script is called by name
if __name__ == '__main__':
	main()

# 0 = '07-Jun-2013'  1 = '15:08:27.870', 
# 2 = 'client'       3 = '172.219.24.53#57546:', 
# 4 = 'query:'       5 = '56.24.219.192.in-addr.arpa', 
# 6 = 'IN'           7 = 'SOA', 
# 8 = '+EDC' 	     9= '(15.254.173.179)' 

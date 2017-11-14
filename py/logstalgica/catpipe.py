#!/usr/bin/env python
# Written By: Glenn
import os
import sys
import re
import datetime
import sys # in case we decide to use STDIN instead to read logs
import time
from datetime import date
YEAR=repr(date.today().year)

for message in sys.stdin:
	messageSplit = message.split()
	
	if len(messageSplit) != 0 :
		MSGLENGTH=len(messageSplit)
		# print messageSplit
		if messageSplit[6] == "Deny":
			#srcADRlist=messageSplit[9].split(":",2)
			#srcIP=srcADRlist[1]
			DateTime = messageSplit[1] + '/' + messageSplit[0] + '/' + "2013" + ':' + messageSplit[2] + " +0200"   

			OUT = messageSplit[9].split("/")[0] + " - -  [" + DateTime + "]" 
			OUT = OUT + " \"GET " + messageSplit[11] + "/" + messageSplit[7] 
			OUT = OUT + " HTTP/1.0\" " + messageSplit[6] + " - " + "\"-\"" + "incoming"
			print  OUT
			#OUTPUT = OUTPUT.' - - ['  
			#OUTPUT = OUTPUT + DateTime 
			#OUTPUT = OUTPUT + '] "GET'
			#print type(messageSplit)
	
# DH-AC-DMZ:172.16.251.6/62809 - -  [11/Jun/2013:07:53:14 +0200]"GET outside:173.194.32.3/443/tcp HTTP/1.0" Deny - "-"incoming 
# 172.16.6.10 - - [11/Jun/2013:06:30:51 +0200] "GET Intern-ASA:172.16.255.36/53 HTTP/1.0" Deny - "-" "172.16.255.36


#10 06:54:06 bp-ekstern
# 0= 'Jun', 1='10', 2='06:54:07', 
# 3= 'bp-ekstern', 4=':', 5='%ASA-4-106023:', 
# 6='Deny', 7='udp', 8='src', 
# 9='DH-AC-DMZ:172.16.6.10/53414', 10='dst', 
# 11='Intern-ASA:172.16.255.35/53', 12='by', 13='access-group', 
# 14='"DH-AC-DMZ_access_in"', 15='[0xafc6791c,', 16='0x0]']


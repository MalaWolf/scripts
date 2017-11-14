#!/usr/bin/env python
# Written By: MW
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
	

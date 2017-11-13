#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Written By: MalaWolf , 2017

import os 
import sys # in case we decide to use STDIN instead to read logs 
import re 
import datetime, time 
import json
import pprint 

# Debug
pp = pprint.PrettyPrinter(indent=4)

def get_keys(dl, keys_list):
    if isinstance(dl, dict):
        keys_list += dl.keys()
        map(lambda x: get_keys(x, keys_list), dl.values())
    elif isinstance(dl, list):
        map(lambda x: get_keys(x, keys_list), dl)
## Debug end

def proto(num):
	protocol={0: "HOPOPT",
			 1: "ICMP",
			 6: "TCP",
			17: "UDP" }
	try:
		num
	except NameError:
		exit(0)
	except ValueError:
		exit(0)	
	else:
		print protocol[num]

# For hver linje/json-object
def main():
	for json_string in sys.stdin:
		try: 
			jdata = json.loads(json_string) 
			#print jdata["timestamp"], jdata["layers"]["ip"]["ip_ip_src"], jdata["layers"]["ip"]["ip_ip_dst"]
		
			# Konverter tid, og 
			# print konvertert flotingpoint timestamp først
			timestamp=str(jdata["timestamp"])
			sec=timestamp[:-3]
			dec=timestamp[-3:]
			millisec=str(sec) + "." + str(dec)
			print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(millisec))), 
			print jdata["layers"]["ip"]["ip_ip_src"], 
			print jdata["layers"]["ip"]["ip_ip_dst"], 
			print jdata["layers"]["ip"]["ip_ip_proto"], 
		
			if proto(int(jdata["layers"]["ip"]["ip_ip_proto"])) != None:
				proto(int(jdata["layers"]["ip"]["ip_ip_proto"]))

			### debugging: print json keys
			#print json.dumps(jdata, indent=4, sort_keys=True)
			#keys = []
			#get_keys(jdata, keys)
			#pp.pprint(keys)

		except ValueError:
			continue

		except KeyError:
			continue

def stop():
	print "..the..end..."

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		stop(0)


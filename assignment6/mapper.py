#!/usr/bin/python

import sys

for line in sys.stdin:
	data = line.strip().split(" ")
    
	if len(data) == 10:
	        date = data[3].strip().split("/")
	if len(date) == 3:
		year = date[2].strip().split(":")
		print year[0]

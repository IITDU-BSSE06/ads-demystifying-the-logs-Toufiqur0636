#!/usr/bin/python

import sys

counter = 0

for line in sys.stdin:
    path = line.strip()
    if path == "/assets/js/the-associates.js":
	counter = counter + 1

print counter

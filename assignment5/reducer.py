#!/usr/bin/python

import sys

path_map = dict()

for line in sys.stdin:
	path = line.strip()
	path_map[path] = path_map.get(path, 0) + 1

print len(path_map)

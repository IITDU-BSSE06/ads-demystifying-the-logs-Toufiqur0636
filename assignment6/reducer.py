#!/usr/bin/python

import sys

path_map = dict()

for line in sys.stdin:
	path = line.strip()
	path_map[path] = path_map.get(path, 0) + 1

popular = max(path_map, key=path_map.get)

print popular

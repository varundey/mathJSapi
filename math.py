#!/usr/bin/env python
import urllib, subprocess
from py_assets.w2n import word2num

def check(query):
	try:
		num =  word2num(query)
		return num
	except:
		return query
		



math  = check(raw_input())

a = subprocess.Popen(["nodejs","js_assets/server.js",math],stdout=subprocess.PIPE)
a.wait()
ans = a.stdout.read().strip()
print ans
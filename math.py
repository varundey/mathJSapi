#!/usr/bin/env python
import urllib, requests
from bottle import route, run

@route('/<query>', method="GET")
def index(query=""):
	math = "http://api.mathjs.org/v1/?expr="+urllib.quote(query)
	ans = requests.get(math).content
	return ans

run(host='localhost', port=8080,debug=True)
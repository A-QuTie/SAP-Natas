#!/usr/bin/python3

import requests

auth = ('natas0', 'natas0')
url = "http://natas0.natas.labs.overthewire.org"
r = requests.get(url, auth=auth)
print(r.text)
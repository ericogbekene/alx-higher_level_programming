#!/usr/bin/python3
""" module to fetch a url """

import urllib.request
import urllib.parse

if __name__ == "__main__":
    resource = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(resource) as response:
        html = response.read()
        print(html)

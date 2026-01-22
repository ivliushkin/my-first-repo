#!/usr/bin/python3
import sys
import urllib.request

with urllib.request.urlopen(sys.argv[1]) as response:
    x_req_id = response.getheader('X-Request-Id')
    if x_req_id is not None:
        print(x_req_id)

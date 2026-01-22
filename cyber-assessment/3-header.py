#!/usr/bin/python3
import sys
import urllib.request

with urllib.request.urlopen(sys.argv[1]) as response:
    xReqId = response.getheader('X-Request-Id')
    if xReqId is None:
        xReqId = ''
    print(xReqId)

#!/bin/env python

import requests
import json
import hashlib
import base64
import time
import hmac

# This script can be used to bulk delete devices using a csv input file

# Account Information for portal
Company = ""
AccessKey = ""
AccessId = ""

# Request Info
httpVerb = 'DELETE'
# Replace the first string with your own file path
f = open("/Users/kendallshearman/lmapi_v3/test.csv", 'r')
deletelist = open("/Users/kendallshearman/lmapi_v3/deletelist.txt", 'a')


idList = f.readlines()
f.close()
s = requests.session()

for i in range(len(idList)):
    if i < (len(idList) - 1):
        cleanId = int(idList[i][:-1])
    else:
        cleanId = int(idList[i])
    #print(cleanId)
    resourcePath = f'/device/devices/{cleanId}'
    data = ''
    url = 'https://' + Company + '.logicmonitor.com/santaba/rest' + resourcePath
    epoch = str(int(time.time() * 1000))
    requestVars = httpVerb + epoch + data + resourcePath
    hmac1 = hmac.new(AccessKey.encode(), msg=requestVars.encode(), digestmod=hashlib.sha256).hexdigest()
    signature = base64.b64encode(hmac1.encode())
    auth = 'LMv1 ' + AccessId + ':' + signature.decode() + ':' + epoch
    headers = {'Content-Type': 'application/json', 'Authorization': auth, 'X-Version': '3'}
    s.headers.update({'Content-Type': 'application/json', 'Authorization': auth, 'X-Version': '3'})
    response = requests.delete(url, data=data, headers=headers)
    deletelist.write("Device with id " + str(cleanId) + " was deleted\n")
    print("Device with id " + str(cleanId) + " was deleted")
    #print('Response Status:', response.status_code)
    #print('Response Body:', response.content)


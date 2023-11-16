#!/bin/env python
import json
import sys

import requests
#import json
import hashlib
import base64
import time
import hmac

# Account Info - replace with your own values
Company = ""
AccessKey = ""
AccessId = ""

# Request Info
httpVerb ='GET'
resourcePath = "/setting/datasources"
data = ''
offset = 0
size = 1000
queryParams = f"?offset={offset}&size={size}"
s = requests.session()

# Construct URL
url = 'https://'+ Company +'.logicmonitor.com/santaba/rest' + resourcePath + queryParams

# Get current time in milliseconds
epoch = str(int(time.time() * 1000))

# Concatenate Request details
requestVars = httpVerb + epoch + data + resourcePath

# Construct signature
hmac1 = hmac.new(AccessKey.encode(), msg=requestVars.encode(), digestmod=hashlib.sha256).hexdigest()
signature = base64.b64encode(hmac1.encode())

# Construct headers
auth = 'LMv1 ' + AccessId + ':' + signature.decode() + ':' + epoch
headers = {'Content-Type': 'application/json', 'Authorization': auth, 'X-Version': '3'}

# Make request to get total
response = requests.get(url, data=data, headers=headers)
respBody = json.loads(response.content)
dataItems = respBody['items']
total = respBody['total']
print(total)
cycles = int(total/size)
print(cycles)


f = open("/Users/kendallshearman/datasourcelist.txt", "a")
# Example: /Users/kendallshearman/datasourcelist.txt

f.write(f"There are currently {total} modules in the {Company} portal listed below.\n")

# Make requests
for i in range(cycles+1):
    queryParams = f"?offset={offset}&size={size}"
    url = 'https://' + Company + '.logicmonitor.com/santaba/rest' + resourcePath + queryParams
    requestVars = httpVerb + epoch + data + resourcePath + queryParams
    hmac1 = hmac.new(AccessKey.encode(), msg=requestVars.encode(), digestmod=hashlib.sha256).hexdigest()
    signature = base64.b64encode(hmac1.encode())
    auth = 'LMv1 ' + AccessId + ':' + signature.decode() + ':' + epoch
    s.headers.update({'Content-Type': 'application/json', 'Authorization': auth, 'X-Version': '3'})
    response = requests.get(url, data=data, headers=headers)
    respBody = json.loads(response.content)
    dataItems = respBody['items']
    for j in range(len(dataItems)):
        content = str(dataItems[j]["id"]) + "\t" + str(dataItems[j]["displayName"]) + "\n"
        print(content)
        f.write(content)
    offset+=1000

f.close()















#!/bin/env python
import json

import requests
#import json
import hashlib
import base64
import time
import hmac
import csv

# - Account Info - replace with your own values
Company = ""
AccessKey = ""
AccessId = ""

# Request Info
httpVerb ='GET'

# This displays all alerts in the portal. Use offset to adjust starting delimiter.

resourcePath = f'/setting/alert/rules'
data = ''

# Construct URL
url = 'https://'+ Company +'.logicmonitor.com/santaba/rest' + resourcePath

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

# Make request
response = requests.get(url, data=data, headers=headers)
dataresponse = json.loads(response.content)
total = dataresponse["total"]
items = dataresponse["items"]

print(f"There are {total} alert rules in {Company}'s portal")
f = open("/Users/kendallshearman/alertrules.csv", "a")

keys = items[0].keys()
write = csv.writer(f)
write.writerow(keys)

for i in range(len(items)):
    for key in items[i]:
        newString = str(items[i][key]) + ", "
        f.write(newString)
        #Printing is just for debugging
        print(newString, end="")
    f.write("\n")
    print("\n")

f.close()











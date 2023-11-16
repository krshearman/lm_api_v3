#!/bin/env python
import json

import requests
#import json
import hashlib
import base64
import time
import hmac

# - Account Info - replace with your own values
Company = ""
AccessKey = ""
AccessId = ""

# Request Info
httpVerb ='GET'
#dsIds = [1626, 699, 697, 412, 302, 200, 199, 370, 301, 407, 405, 50, 1255, 525, 249, 1509, 548, 156, 638, 609, 1501, 1635, 1630, 201, 1294]

dsId = #<REPLACE WITH YOUR DS ID>
resourcePath = f'/setting/datasources/{dsId}'
data = ''
queryParams = '?format=json&v=3'

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

# Make request
response = requests.get(url, data=data, headers=headers)
parseResp = json.loads(response.content)
dsName = parseResp['name']
#print(dsName)

# Replace with the path to your own directory, i.e. /Users/kendallshearman/dsdltest/
f = open(f"<REPLACE WITH YOUR PATH>{dsName}.xml", "x")

respStr = str(json.loads(response.content))
f.write(respStr)
f.close()

# Print status and body of response
print('Response Status:', response.status_code)
print('Response Body:', response.content)



















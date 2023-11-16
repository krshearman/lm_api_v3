#!/bin/env python

import requests
import json
import hashlib
import base64
import time
import hmac

# Account Info
Company = ""
AccessKey = ""
AccessId = ""

# Request Info
httpVerb ='POST'

# Identify dashboard group
dbGroupId = 26

resourcePath = f'/dashboard/dashboards/{dbGroupId}/clone'
data = '{"name":"Collectors_clone_007","description":"Status and critical metrics of your LogicMonitor Collectors.","widgetTokens":[{"name":"defaultDevice","value":"*"},{"name":"defaultResourceGroup","value":"Devices by Type/Collectors"},{"name":"defaultResourceName","value":"*"}],"sharable":true,"groupName":"LogicMonitor Dashboards/LogicMonitor","groupId":3,"widgetsConfig":{"406":{"col":1,"sizex":12,"row":1,"sizey":2},"407":{"col":1,"sizex":12,"row":30,"sizey":4},"408":{"col":4,"sizex":3,"row":23,"sizey":4},"409":{"col":7,"sizex":3,"row":23,"sizey":4},"410":{"col":1,"sizex":3,"row":23,"sizey":4},"411":{"col":1,"sizex":6,"row":27,"sizey":3},"412":{"col":8,"sizex":5,"row":3,"sizey":3},"413":{"col":7,"sizex":6,"row":27,"sizey":3},"414":{"col":8,"sizex":5,"row":6,"sizey":3},"415":{"col":10,"sizex":3,"row":15,"sizey":4},"416":{"col":10,"sizex":3,"row":11,"sizey":4},"417":{"col":10,"sizex":3,"row":23,"sizey":4},"418":{"col":1,"sizex":5,"row":19,"sizey":4},"419":{"col":6,"sizex":7,"row":19,"sizey":4},"420":{"col":6,"sizex":4,"row":11,"sizey":4},"421":{"col":6,"sizex":4,"row":15,"sizey":4},"422":{"col":1,"sizex":5,"row":11,"sizey":8},"423":{"col":9,"sizex":4,"row":9,"sizey":2},"424":{"col":5,"sizex":2,"row":9,"sizey":2},"425":{"col":1,"sizex":2,"row":9,"sizey":2},"426":{"col":3,"sizex":2,"row":9,"sizey":2},"427":{"col":1,"sizex":7,"row":3,"sizey":6},"428":{"col":7,"sizex":2,"row":9,"sizey":2},"2755":{"col":1,"sizex":6,"row":34,"sizey":7},"2757":{"col":7,"sizex":6,"row":34,"sizey":7}},"widgetsOrder":""}'

# Construct URL
url = 'https://'+ Company +'.logicmonitor.com/santaba/rest' + resourcePath

# Get current time in milliseconds
epoch = str(int(time.time() * 1000))

# Concatenate Request details
requestVars = httpVerb + epoch + data + resourcePath

# Construct signature
hmac1 = hmac.new(AccessKey.encode(),msg=requestVars.encode(),digestmod=hashlib.sha256).hexdigest()
signature = base64.b64encode(hmac1.encode())

# Construct headers
auth = 'LMv1 ' + AccessId + ':' + signature.decode() + ':' + epoch
headers = {'Content-Type': 'application/json', 'Authorization': auth, 'X-Version': '3'}

# Make request
response = requests.post(url, data=data, headers=headers)

# Print status and body of response
print('Response Status:', response.status_code)
print('Response Body:', response.content)
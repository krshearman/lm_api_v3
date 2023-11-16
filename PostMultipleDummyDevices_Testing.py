####### Logicmonitor 2022 - Peter Bertholdi #######

# !/bin/env python

# generic
import requests
import json
import hashlib
import base64
import time
import hmac
import sys

#Account Info
Company = ""
AccessKey = ""
AccessId = ""

# Json template builder
hostGroup_id = 246
preferredCollector_id = 5

# device name builder
Devicename = '"'
DeviceUrl = '"'  # if you wish to only have a numbered device name please leave the quote between the apostrophe's '"'

# Amount of devices to add

DeviceAmount = 10


# notify of issue
if AccessId == '':
    sys.exit("Please ensure AccessId credentials are added before continuing")

if AccessKey == '':
    sys.exit("Please ensure AccessKey credentials are added before continuing")

if Company == '':
    sys.exit("Please ensure company name is added before continuing")

# Request

requestverb = 'POST'
requestpath = '/device/devices'
requestversion = '3'
requestquery = ''


# LMv1 token gen

def GenericAPI(verb, path, version, query, data):
    # Construct URL
    if not verb.isupper():
        sys.exit("Please ensure your verb is entered in upper case")

    if verb == "GET" or verb == "DELETE":
        if not data == '':
            sys.exit("Please ensure the requestdata variable is blank when making GET or DELETE requests")

    if not query:
        url = 'https://' + Company + '.logicmonitor.com/santaba/rest' + path + '?v=' + version
    else:
        url = 'https://' + Company + '.logicmonitor.com/santaba/rest' + path + '?v=' + version + '&' + query

    # Get current time in milliseconds
    epoch = str(int(time.time() * 1000))
    # Concatenate Request details
    requestVars = verb + epoch + data + path
    # Construct signature
    hmac1 = hmac.new(AccessKey.encode(), msg=requestVars.encode(), digestmod=hashlib.sha256).hexdigest()
    signature = base64.b64encode(hmac1.encode())
    # Construct headers
    auth = 'LMv1 ' + AccessId + ':' + signature.decode() + ':' + epoch
    headers = {'Content-Type': 'application/json', 'Authorization': auth}

    # Make request
    print(url)
    if verb == "GET":
        response = requests.get(url, data=data, headers=headers)
    if verb == "PUT":
        response = requests.put(url, data=data, headers=headers)
    if verb == "PATCH":
        response = requests.patch(url, data=data, headers=headers)
    if verb == "POST":
        response = requests.post(url, data=data, headers=headers)
    if verb == "DELETE":
        response = requests.delete(url, data=data, headers=headers)

    # Print status and body of response
    print('Response Status:', response.status_code)
    print('Response Body:', response.content)


json_template_1 = '{"name":"%%deviceUrl%%","displayName":"%%deviceUrl%%","hostGroupIds":'f'"{hostGroup_id}","preferredCollectorId":'f'"{preferredCollector_id}"'"}"
json_final = (json_template_1)
devicename_final = f"{Devicename}%02d{DeviceUrl}"
total = DeviceAmount + 1

for demo in range(1, (total)):
    json_payload = json_final.replace('"%%deviceUrl%%"', devicename_final % (demo,))
    GenericAPI(requestverb, requestpath, requestversion, requestquery, json_payload)




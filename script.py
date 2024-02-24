import requests
import time
import json

#verifies service status and returns json file with time and status codes

currentTime = time.strftime("%H:%M:%S")
mainResponse = requests.get('https://ai-plans.com/')
apiResponse = requests.get('https://pb.ai-plans.com/api/status')
devResponse = requests.get('https://dev.ai-plans.com/')
v2Response = requests.get('https://v2.ai-plans.com/')


dictionary = {
    "time": currentTime,
    "mainStatus": mainResponse.status_code,
    "apiStatus": apiResponse.status_code,
    "devStatus": devResponse.status_code,
    "v2Status": v2Response.status_code
    }

with open('status.json', 'a') as statusFile:
    json.dump(dictionary, statusFile)
    statusFile.write('\n')
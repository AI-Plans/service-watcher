import requests
import time
import json

#verifies api status and returns json file with time and status code

response = requests.get('https://pb.ai-plans.com/api/status')
currentTime = time.strftime("%H:%M:%S")

dictionary = {"time": currentTime,"status": response.status_code}

with open('status.json', 'a') as statusFile:
    json.dump(dictionary, statusFile)
    statusFile.write('\n')

#print ('Status updated')
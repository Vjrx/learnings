import requests
import json

url = "https://www.fast2sms.com/dev/bulk"
payload = "sender_id=FSTSMS&message=test&language=english&route=p&numbers=7010780953"
headers = {
'authorization': "53CZHOqWRhUnQmE68rIABTkV2z7ioDS9sPjulKaNGXdeMp4c0xAOwrvx8mUatf96JCeilGsTFybBI0VR",
'Content-Type': "application/x-www-form-urlencoded",
'Cache-Control': "no-cache",
}
response = requests.request("POST", url, data=payload, headers=headers)
print(response.text)
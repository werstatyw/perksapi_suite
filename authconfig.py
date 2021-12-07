import requests
import json
import scriptconfig as cfg
from types import SimpleNamespace
url = cfg.url+"Authorize"
print(url)
logindata = {
  'email': cfg.email,
  'password': cfg.pwd
}
payload = json.dumps(logindata)

#payload='{"message":"' +str(s)+ '"}'
#payload['email']=cfg.email
#payload['password']=cfg.pwd
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

#print(response.text)

#bearer = response.text[:response.text.rfind("refreshToken")]

#s[:s.rfind("&")]

#print(bearer[15:])
#print(bearer)

#data1 = json.load(response.text)
x = json.loads(response.text, object_hook=lambda d: SimpleNamespace(**d))
bearer = x.accessToken
print(bearer)

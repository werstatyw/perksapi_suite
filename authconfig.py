import requests
import json
from types import SimpleNamespace
url = "https://test3.perksdev.com/api/v1/Authorize"

payload = json.dumps({
  "email": "psst@tsst.com",
  "password": "Test123!"
})
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

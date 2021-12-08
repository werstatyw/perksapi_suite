import requests
import json
import scriptconfig as cfg
from types import SimpleNamespace
url = cfg.url+"Authorize"
logindata = {
  'email': cfg.email,
  'password': cfg.pwd
}
payload = json.dumps(logindata)

headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

x = json.loads(response.text, object_hook=lambda d: SimpleNamespace(**d))
bearer = x.accessToken
print(bearer)

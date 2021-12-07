#!/usr/bin/env python
def auth_req():
    import requests
    import json
    import scriptconfig as cfg

    url = cfg.url+"Authorize"

    logindata = {
   'email': cfg.email,
   'password': cfg.pwd
    }
    payload = json.dumps(logindata)
    headers = {"Content-Type": "application/json"}

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.status_code
    
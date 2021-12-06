#!/usr/bin/env python
def auth_req():
    import requests
    import json
    import scriptconfig as cfg
    from types import SimpleNamespace

    url = cfg.url+"Authorize"

    payload = json.dumps({"email": "psst@tsst.com", "password": "Test123!"})
    headers = {"Content-Type": "application/json"}

    response = requests.request("POST", url, headers=headers, data=payload)

    x = json.loads(response.text, object_hook=lambda d: SimpleNamespace(**d))

    bearer = x.accessToken

    return response.status_code
    
#auth_req()

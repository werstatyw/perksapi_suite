def rfr_token():
    import requests
    import json
    import scriptconfig as cfg, authconfig as auth

    url = cfg.url + "RefreshToken"

    rfrtoken = {"accessToken": auth.bearer, "refreshToken": auth.refreshtoken}

    payload = json.dumps(rfrtoken)
    headers = {"Content-Type": "application/json"}

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.status_code

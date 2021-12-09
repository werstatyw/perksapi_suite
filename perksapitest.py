def basictest():
    import requests
    import scriptconfig as cfg, authconfig as auth

    url = cfg.url + "test"
    payload = ""
    headers = {}
    headers["Authorization"] = "Bearer " + auth.bearer

    response = requests.request("GET", url, headers=headers, data=payload)
    return response.text

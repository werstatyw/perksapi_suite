def user_get():
    import requests
    import scriptconfig as cfg, authconfig as auth

    url = cfg.url + "User"

    payload = {}
    headers = {}
    headers["Authorization"] = "Bearer " + auth.bearer

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)
    return response.status_code

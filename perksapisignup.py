def sign_up():
    import requests
    import json
    import scriptconfig as cfg, authconfig as auth

    url = cfg.url + "SignUp"
    print(cfg.code)
    logindata = {
        "code": cfg.code,
        "email": cfg.randomemail,
        "password": cfg.pwd,
        "firstName": cfg.firstName,
        "lastName": cfg.lastName,
        "employeeTypeId": cfg.employeeTypeId,
    }
    payload = json.dumps(logindata)

    headers = {}
    headers["Authorization"] = "Bearer " + auth.bearer
    headers["Content-Type"] = "application/json"

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.status_code

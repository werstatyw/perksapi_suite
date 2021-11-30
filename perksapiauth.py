def auth_req():
    import requests
    import json

    url = "https://test3.perksdev.com/api/v1/Authorize"

    payload = json.dumps({
      "email": "psst@tsst.com",
      "password": "Test123!"
    })
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.status_code
    
auth_req()

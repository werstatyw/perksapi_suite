def basictest():
    import requests
    #import json
    import scriptconfig as cfg, authconfig as auth
    
    url = cfg.url+"test"
    payload = ""
    """""
    headers = {
    'Authorization': 'Bearer {auth.bearer}'
    }
    """

    headers = {}
    headers['Authorization']='Bearer ' + auth.bearer
 
    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)
    #print(auth.url)
    return(response.text)
    print(response.text)
#basictest()
    
def basictest():
    import requests
    import json
    import scriptconfig as cfg
    import perksapiauth as auth

    url = cfg.url+"test"
    payload = ""
    headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6InBzc3RAdHNzdC5jb20iLCJuYW1laWQiOiIzMzk4OTkyYS1hOWNkLTQyMWQtOGFhOS1hNjVkYjlmNzllOTQiLCJlbWFpbCI6InBzc3RAdHNzdC5jb20iLCJUZW5hbnRJZCI6IjkiLCJuYmYiOjE2Mzg0NjM4NzEsImV4cCI6MTY0MTA1NTg3MSwiaWF0IjoxNjM4NDYzODcxLCJpc3MiOiJQRVJLUyBtb2JpbGUgZGV2In0.ez_ZB3x5hNAXYp4CdEDJJ3VzPdtuOQLytdfwcq3fbOc',
    'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    #print (auth.response.text)
    return response.text

#basictest()
    
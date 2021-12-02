def basictest():
    import requests
    import json

    url = "https://test3.perksdev.com/api/v1/test"

    payload = json.dumps({
    "email": "psst@tsst.com",
    "password": "Test123!"
    })
    headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6InBzc3RAdHNzdC5jb20iLCJuYW1laWQiOiIzMzk4OTkyYS1hOWNkLTQyMWQtOGFhOS1hNjVkYjlmNzllOTQiLCJlbWFpbCI6InBzc3RAdHNzdC5jb20iLCJUZW5hbnRJZCI6IjkiLCJuYmYiOjE2Mzg0NjM4NzEsImV4cCI6MTY0MTA1NTg3MSwiaWF0IjoxNjM4NDYzODcxLCJpc3MiOiJQRVJLUyBtb2JpbGUgZGV2In0.ez_ZB3x5hNAXYp4CdEDJJ3VzPdtuOQLytdfwcq3fbOc',
    'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.text

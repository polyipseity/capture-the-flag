from sys import argv
from requests import post

if __name__ == "__main__":
    base_url = "https://boilerscasino-19f92d3631a96d90.instancer.b01lersc.tf"
    with post(
        f"{base_url}/login", json={"username": "admin", "password": argv[1]}
    ) as req:
        req.raise_for_status()
        print(req.json()["jwt"])

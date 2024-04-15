from pathlib import Path
from jwt import decode, encode

if __name__ == "__main__":
    private_key = Path("private_key.pem")
    public_key = Path("public_key.png")
    jwt = encode(
        payload={"key": "value"},
        key=private_key.read_bytes(),
        algorithm="RS256",
        headers={"kid": str(public_key)},
    )
    print(decode(jwt=jwt, key=public_key.read_bytes(), algorithms=["RS256"]))

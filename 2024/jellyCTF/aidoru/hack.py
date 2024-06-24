from hashlib import md5
from requests import get


if __name__ == "__main__":
    with get(
        f"https://aidoru.jellyc.tf/static/secret_data/{md5(b"jelly").digest().hex()}.json"
    ) as req:
        print(req.text)

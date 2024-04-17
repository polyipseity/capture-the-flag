from requests import post

with post("http://embed-flow.ictf5.ninja/", data={"guess": None}) as req:
    print(req.text)

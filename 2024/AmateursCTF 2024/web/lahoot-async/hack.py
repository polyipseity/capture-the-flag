from json import loads
from time import sleep
from uuid import uuid4
from requests import get, post

BASE_URL = "http://lahoot-async.amt.rs"
DATA_ID_START_TEXT = 'data-id = "'
DATA_ID_END_TEXT = '"'
QUESTION_NO = 200

if __name__ == "__main__":
    with post(f"{BASE_URL}/session", data={"username": str(uuid4())[:16]}) as req:
        req.raise_for_status()
        session = req.history[0].cookies["session"]
        data_id_idx = req.text.find(DATA_ID_START_TEXT) + len(DATA_ID_START_TEXT)
        data_id = req.text[data_id_idx : req.text.find(DATA_ID_END_TEXT, data_id_idx)]
    print(f"session: {session}")
    for idx in range(QUESTION_NO):
        print(f"question {idx + 1}")
        with get(f"{BASE_URL}/api/question/{data_id}") as req:
            req.raise_for_status()
            answer = loads(req.text)["correctAnswer"]
        print(f"{data_id}: {answer}")
        if idx == QUESTION_NO - 1:
            break
        with post(
            f"{BASE_URL}/question",
            cookies={"session": session},
            data={"answer": answer},
        ) as req:
            req.raise_for_status()
            data_id_idx = req.text.find(DATA_ID_START_TEXT) + len(DATA_ID_START_TEXT)
            data_id = req.text[
                data_id_idx : req.text.find(DATA_ID_END_TEXT, data_id_idx)
            ]
        sleep(0.1)

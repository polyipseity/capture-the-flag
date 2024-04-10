from pathlib import Path
from socket import AF_INET, socket
from ssl import SOCK_STREAM
from time import sleep

if __name__ == "__main__":
    with socket(AF_INET, SOCK_STREAM) as conn:
        conn.connect(("chal.amt.rs", 1818))

        def recv():
            print(conn.recv(65536).decode("utf-8"), end="")

        def send(payload: str):
            if payload:
                print(payload)
            conn.send(f"{payload}\n".encode())

        recv()
        send(Path("hack_content2.py").read_text())
        recv()
        send("<END>")
        sleep(3)
        recv()
        recv()

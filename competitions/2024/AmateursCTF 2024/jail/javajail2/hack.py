from pathlib import Path
from socket import AF_INET, socket
from ssl import SOCK_STREAM

if __name__ == "__main__":
    with socket(AF_INET, SOCK_STREAM) as conn:
        conn.connect(("chal.amt.rs", 2104))

        def recv():
            print(conn.recv(65536).decode("utf-8"))

        def send(payload: str):
            if payload:
                print(payload)
            conn.send(f"{payload}\n".encode())

        recv()
        send(Path("hack.java").read_text())
        send("--EOF--")
        recv()

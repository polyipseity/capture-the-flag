import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("ash-chal.firebird.sh", 36004))
while 1:
    data = s.recv(1024)
    print(data.decode("utf-8"))
    if not data:
        break
    data_s = data.decode("utf-8")
    if "y/n" in data_s:
    	s.sendall(b"y\n")
    	continue
    data = data_s.strip().split("\n")[-1].encode("utf-8") + b"\n"
    print(data)
    s.sendall(data)
s.close()

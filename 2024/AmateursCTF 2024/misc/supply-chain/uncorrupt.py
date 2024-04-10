from pathlib import Path


if __name__ == "__main__":
    solution = Path("bad-fixing.tar.xz").read_bytes()
    ret = bytearray()

    for byte in solution:
        if byte == 0x9:
            ret.append(0x20)
            print("0x09 converted to 0x20")
        elif byte == 0x20:
            ret.append(0x9)
            print("0x20 converted to 0x09")
        elif byte == 0x2D:
            ret.append(0x5F)
            print("0x2d converted to 0x5f")
        elif byte == 0x5F:
            ret.append(0x2D)
            print("0x5f converted to 0x2d")
        else:
            ret.append(byte)

    Path("good-fixing.tar.xz").write_bytes(ret)

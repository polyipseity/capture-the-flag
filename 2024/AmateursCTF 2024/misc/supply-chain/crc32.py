from zlib import crc32


if __name__ == "__main__":
    print("%x" % crc32(b"\x00\x01"))
    print("%x" % crc32(b"\x00\x04"))
    print("%x" % crc32(b"\x02\x00\x00\x00\x00\x01"))
    print("%x" % crc32(b"\x02\x00\x00\x00\x00\x04"))

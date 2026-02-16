import itertools

flag = bytes(
    itertools.chain.from_iterable(
        (int(byte, 16) for byte in line.split(" "))
        for line in """0C 5C 60 20 69 63 64 0F
4F 1E 33 3A 68 2A 7C D9
D5 D0 C9 E7 C3 F0 BC AB
9B D7 98 8B AF B0 F8 47
49 16 49 68 00 00 00 00
00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00""".splitlines()
    )
)
key = bytes(
    itertools.chain.from_iterable(
        (int(byte, 16) for byte in line.split(" "))
        for line in """7B 3D 14 43 01 43 5E 2F
27 6A 47 4A 1B 10 53 F6
AC BF BC 93 B6 DE DE CE
B4 B3 C9 FC 9B C7 C1 10
2E 4E 2A 39""".splitlines()
    )
)

print(f"flag: {flag}")
print(f"key: {key}")
print(f"ans: {bytes(a ^ b for a, b in zip(key, flag))}")

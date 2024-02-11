import hashlib
import itertools
from random import *
from PIL import Image

im = Image.open("encrypted_flag.png")
pix = im.load()
width, height = im.size

key = "firebird_is_the_best!!UwU"

seed(hashlib.md5(key.encode()).hexdigest().encode())

for x in reversed(range(width)):
    for y in reversed(range(height)):
        pix[x, y] = (
            pix[x, y][0] ^ ord(key[(x + y) % len(key)]),
            pix[x, y][1] ^ ord(key[(x + y) % len(key)]),
            pix[x, y][2] ^ ord(key[(x + y) % len(key)]),
        )

randoms = list(
    itertools.chain.from_iterable(
        (randint(0, width), randint(0, height)) for _ in range(width * height * 3)
    )
)

for x in reversed(range(width)):
    for y in reversed(range(height)):
        randoms2 = list[int]()
        for _ in range(6):
            randoms2.insert(0, randoms.pop())
        pix[x, y] = (
            pix[x, y][0]
            ^ pix[(x + randoms2[0]) % width, (y + randoms2[1]) % height][0],
            pix[x, y][1]
            ^ pix[(x + randoms2[2]) % width, (y + randoms2[3]) % height][1],
            pix[x, y][2]
            ^ pix[(x + randoms2[4]) % width, (y + randoms2[5]) % height][2],
        )

assert not randoms

im.save("decrypted_flag.png", format="png")

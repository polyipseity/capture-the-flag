from PIL import Image

im = Image.open("empty_encrypted.png")
pix = im.load()
width, height = im.size
key = ""

for x in range(width):
    key += chr(pix[x, 0][0])

print(key)
# firebird_is_the_best!!UwU

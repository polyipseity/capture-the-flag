from PIL import Image
from PIL.TiffTags import TAGS
import cv2
import pandas

with Image.open("aura.tif") as img:
    meta_dict = {TAGS[key]: img.tag[key] for key in img.tag.keys()}

# print(meta_dict)

# 896x896 -> 0b1110000000

image = cv2.imread("aura.tif", cv2.IMREAD_UNCHANGED)
# for row_num, row in enumerate(image):
#     if row_num > 0:
#         continue
#     for col_num, pix in enumerate(row):
#         print(tuple(map(lambda v: int("{0:b}".format(v)[-1], 2), pix)))
image2 = image & 1
print(image2)
df = pandas.DataFrame(image2[:,:,0])

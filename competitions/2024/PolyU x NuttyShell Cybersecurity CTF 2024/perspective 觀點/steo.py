import cv2
import os

os.makedirs("steo", exist_ok=True)

image = cv2.imread("perspective.jpg", cv2.IMREAD_UNCHANGED)

for bits in range(4):
    for idx, clr in enumerate("bgr"):
        cv2.imwrite(
            f"steo/{clr}@{bits + 1}.png", (image[:, :, idx] & 2**bits) * (256 / 2**bits)
        )

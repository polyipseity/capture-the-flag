from pathlib import Path
from cv2 import IMREAD_UNCHANGED, imread, imwrite
import numpy as np

car1 = imread("car1.png", IMREAD_UNCHANGED)
car2 = imread("car2.png", IMREAD_UNCHANGED)

car1_complex = car1.astype(np.int16)
car2_complex = car2.astype(np.int16)
Path("car1.png.samples.txt").write_text(str(car1_complex))
Path("car2.png.samples.txt").write_text(str(car2_complex))

print(np.all(car1_complex[..., 1] == car1_complex[..., 2]))
print(np.all(car2_complex[..., 1] == -car2_complex[..., 2]))
# interesting, satisfies https://en.wikipedia.org/wiki/Holomorphic_function#Definition

exit()

imwrite("unknown.png", car1_complex[..., 0].astype(np.float64) / 4)
imwrite("dv_dy.png", car1_complex[..., 2].astype(np.float64) * 4 + 128)
imwrite("du_dx.png", car1_complex[..., 1].astype(np.float64) * 4 + 128)
imwrite("du_dy.png", car2_complex[..., 2].astype(np.float64) * 4 + 128)
imwrite("dv_dx.png", car2_complex[..., 1].astype(np.float64) * 4 + 128)
# wonder why car2.png red channel is all 0... is that supposed to be the flag image?

imwrite("dv_dy.0.png", (car1_complex[..., 2].astype(np.float64) == 0) * 256)
imwrite("du_dx.0.png", (car1_complex[..., 1].astype(np.float64) == 0) * 256)
imwrite("du_dy.0.png", (car2_complex[..., 2].astype(np.float64) == 0) * 256)
imwrite("dv_dx.0.png", (car2_complex[..., 1].astype(np.float64) == 0) * 256)


def inspect_file(array, filename: str):
    Path(filename).write_text(
        "\n".join(
            ", ".join(
                " ".join(str(channel).zfill(4) for channel in pixel) for pixel in row
            )
            for row in array
        )
    )


inspect_file(car1_complex, "car1.png.data.txt")

# try reconstruct image from derivative
real_part = np.zeros((1080, 1920), dtype=np.float64)
accu = 0
for ii in range(1920):
    real_part[-1][ii] = (accu := accu + car1_complex[-1, ii, 1])
for ii in range(2, 1081):
    real_part[-ii] = real_part[-ii + 1] + car2_complex[-ii, ..., 2]
img_part = np.zeros((1080, 1920), dtype=np.float64)
accu = 0
for ii in range(1920):
    img_part[-1][ii] = (accu := accu + car2_complex[-1, ii, 1])
for ii in range(2, 1081):
    img_part[-ii] = img_part[-ii + 1] + car1_complex[-ii, ..., 2]

real_part -= np.average(real_part)
real_part -= np.min(real_part)
real_part /= np.max(real_part)
imwrite("real_part.png", real_part * 256)
img_part -= np.average(img_part)
img_part -= np.min(img_part)
img_part /= np.max(img_part)
imwrite("img_part.png", img_part * 256)

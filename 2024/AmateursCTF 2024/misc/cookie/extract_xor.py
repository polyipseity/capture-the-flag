from pathlib import Path
from cv2 import imread


if __name__ == "__main__":
    image = imread("view_out_image.png")
    ret = list[list[str]]()
    for y in range(16, 8626 + 1, 14):
        ret2 = list[str]()
        ret.append(ret2)
        for x in range(3, 8613 + 1, 14):
            yy = y
            if x == 3:
                yy += 1
            yy += (x - 3) // 2
            ret2.append("1" if (image[yy][x] == 255).all() else "0")
            ret2.append(
                "X" if (image[yy - (1 if x == 3 else 0)][x + 5] == 0).all() else ">"
            )
    Path("xor.txt").write_text("\n".join("".join(ret2) for ret2 in ret))

from pathlib import Path
import numpy as np
from cv2 import imwrite


if __name__ == "__main__":
    server_map = Path("out.txt").read_text()
    w, l, server_map = server_map.split("/")
    qq = {"$0": 255, ";3": 0, "g0": 127, "^0": 63}

    idx = 0
    out = list[list[int]]()
    for l_idx in range(int(l)):
        out2 = list[int]()
        out.append(out2)
        for w_idx in range(int(w)):
            out2.append(qq[server_map[idx : idx + 2]])
            idx += 2
    imwrite("view_out_image.png", np.array(out))

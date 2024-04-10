from copy import deepcopy
from pathlib import Path
import numpy as np
from cv2 import imwrite
from tqdm.auto import tqdm


if __name__ == "__main__":
    server_map = Path("out.txt").read_text()
    w, l, server_map = server_map.split("/")
    w, l = int(w), int(l)
    qq = {"$0": 255, ";3": -1, "g0": 127, "^0": 0}

    idx = 0
    out = list[list[int]]()
    with tqdm(total=w * l) as prog:
        for l_idx in range(l):
            out2 = list[int]()
            out.append(out2)
            for w_idx in range(w):
                out2.append(qq[server_map[idx : idx + 2]])
                idx += 2
            prog.update(w)

    # -1 is unconfirmed black, 0 is confirmed black
    neighbors = list((idx, idx2) for idx in range(-1, 2) for idx2 in range(-1, 2))
    reversed_out = list(map(list, out))
    reversed_out[-4][-4] = 255
    with tqdm(total=(w - 2) * (l - 2)) as prog:
        for l_idx in reversed(range(1, l - 1)):
            for w_idx in reversed(range(1, w - 1)):
                if reversed_out[l_idx][w_idx] == 255:
                    count = 0
                    for y, x in neighbors:
                        match reversed_out[l_idx + y][w_idx + x]:
                            case 255:
                                count += 1
                            case _:
                                pass
                    if count > 1:
                        print("error")
                    for y, x in neighbors:
                        match reversed_out[l_idx + y][w_idx + x]:
                            case -1:
                                if count < 1:
                                    reversed_out[l_idx + y][w_idx + x] = 255
                                    count += 1
                                else:
                                    reversed_out[l_idx + y][w_idx + x] = 0
                            case _:
                                pass
                elif reversed_out[l_idx][w_idx] == 0:
                    count = 0
                    for y, x in neighbors:
                        match reversed_out[l_idx + y][w_idx + x]:
                            case 255:
                                count += 1
                            case _:
                                pass
                    if count > 0:
                        print("error")
                    for y, x in neighbors:
                        match reversed_out[l_idx + y][w_idx + x]:
                            case -1:
                                reversed_out[l_idx + y][w_idx + x] = 0
                            case _:
                                pass
                prog.update()

    imwrite("reverse_play.png", np.array(reversed_out))

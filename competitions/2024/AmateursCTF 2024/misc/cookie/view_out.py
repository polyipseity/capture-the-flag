from pathlib import Path


if __name__ == "__main__":
    server_map = Path("out.txt").read_text()
    w, l, server_map = server_map.split("/")
    qq = {"$0": "S", ";3": " ", "g0": ".", "^0": "X"}

    idx = 0
    with open("view_out.txt", "w+t") as out:
        for l_idx in range(int(l)):
            for w_idx in range(int(w)):
                out.write(qq[server_map[idx : idx + 2]])
                idx += 2
            out.write("\n")

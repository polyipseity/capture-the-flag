from csv import reader
from itertools import permutations

write_index = 4
data_index = 5
indices = [1, 2, 3, 8]

with open("decode.txt", "wt") as out:
    for indices_p in permutations(indices, len(indices)):
        nibbles = list[str]()
        with open("Sniffed_Conversations.csv", newline="") as csvfile:
            spamreader = reader(csvfile)
            for row in spamreader:
                row = tuple(map(str.strip, row))
                if row[data_index] == "0":
                    continue
                if row[write_index] == "1":
                    nibbles.append("".join(row[index] for index in indices_p))

        nibbles_iter = iter(nibbles)
        nibbles_combined = tuple(map("".join, zip(*(nibbles_iter,) * 2)))
        out.write("".join(chr(int(byte, 2)) for byte in nibbles_combined))
        out.write("\n")

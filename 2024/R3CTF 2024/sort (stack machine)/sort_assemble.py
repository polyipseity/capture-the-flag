from base64 import b64encode
from pathlib import Path

MAPPING = {
    "PUSHL": 255,
    "PUSH": 254,
    "SWAP": 253,
    "DUP": 252,
    "DUP2": 251,
    "DUP3": 250,
    "DUP4": 249,
    "POP2": 0,
    "ADD": 1,
    "SUB": 2,
    "MUL": 3,
    "DIV": 4,
    "REM": 5,
    "AND": 6,
    "OR": 7,
    "XOR": 8,
    "SHL": 9,
    "LT": 10,
    "EQ": 11,
    "GT": 12,
    "LTE": 13,
    "GTE": 14,
    "NEQ": 15,
    "DEBUG": 248,
}

# 32~127
# 0b00100000~0b01111111
if __name__ == "__main__":
    codes = Path("sort.txt").read_text().split()
    Path("sort_assembly.txt").write_text(
        b64encode(bytes(int(MAPPING.get(code, code)) for code in codes)).decode() + "\n"
    )


# https://bertdobbelaere.github.io/sorting_networks.html#N30L172D14
# https://stackoverflow.com/a/57282727
# https://stackoverflow.com/a/66432167
# https://stackoverflow.com/q/514435

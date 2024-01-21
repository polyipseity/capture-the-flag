import pandas
import re

with open("data.txt") as f:
    lines = f.readlines()

data = list[str]()
for line in lines:
    datum = line.split("      ")
    if len(datum) == 1:
        data.append("INTERRUPT")
        continue
    if datum[1][4:6] == "00":
        continue
    data.append(chr(int(datum[1][4:6], 16)))
    # popped = data.pop()
    # if popped == "S":
    #   continue
    # data.append(popped)

print(pandas.Series(data).value_counts())

# V (0x56) -> { (0x7b)
# (0x06) -> } (0x7d)

# U (0x55) -> d (0x64) ?
# ) (0x29) -> } (0x7d) ?

# dic = {"\x06": "}", "V": "{", "U": "d", "a": "r", "`": "i", "T": "b", "Y": "e", "\\": "r", "_": "i", "^": "_", "Z": "f"}
dic = {"V": "{", "\x06": "}"}
dic = {
    "\x10": "q",
    "\x11": "w",
    "\x12": "e",
    "\x13": "r",
    "\x14": "t",
    "\x15": "y",
    "\x16": "u",
    "\x17": "i",
    "\x18": "o",
    "\x19": "p",
    "\x1a": "[",
    "\x1b": "]",
    "\x1c": "ENTER",
    "\x1d": "LCTRL",
    "\x1e": "a",
    "\x1f": "s",
    "\x20": "d",
    "\x21": "f",
    "\x22": "g",
    "\x23": "h",
    "\x24": "j",
    "\x25": "k",
    "\x26": "l",
    "\x27": ":",
    "\x28": "'",
    "\x29": "`",
    "\x2a": "LSHIFT",
    "\x2b": "\\",
    "\x2c": "Z",
    "\x50": "DOWN",
    "\x51": "PAGEDOWN",
    "\x52": "INS",
    "\x53": "DEL",
    "\x54": "SYSRQ",
    "\x57": "F11",
    "\x58": "F12",
    "\x59": "1",
}
data = [dic.get(a, a) for a in data]
print(data)
print(re.sub(".?INTERRUPT", "", "".join(data)))

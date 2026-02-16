import pandas
import typing

data = "UTS_\\Y]^T]ZS_\\YTa][`aUTS_\\YZ[S_\\YZ[^a`T]ZS_\\YTa][Ua^[ZY\\_`T_\\Z_\\YZ[^a`S_\\Y]^[YZ[_\\]a^[ZY_\\YZ[^a`_\\YZ[^aYZ[a`_\\YZ[T_\\Ya^[]_\\Y][WXYZ[UTS_`a^[ZY`aUTS_\\YZ[`aUTS_\\YZ[YZ[S_\\YT`aUVWX_\\]a^[ZYYZ[S_\\Ya][STUa_`^[ZY_\\]a^[ZYS_\\YZ[^a`_\\YZ[^a`T_\\Ya^[]S_\\YTa][Ua^[ZY\\_`Ta^Z((\x06"
frame_size = 4
frames = list[str]()
for idx in range(len(data) // frame_size):
    frames.append(data[idx * frame_size : (idx + 1) * frame_size])

print(" ".join(frames))
# print(pandas.Series(frames).value_counts())

# backspaced = list[str]()
# for a in frames:
#     if a == "_\\YZ":
#         backspaced.pop()
#         continue
#     backspaced.append(a)
# print(" ".join(backspaced))
# print(pandas.Series(backspaced).value_counts())

encoding = {"Z((\x06": "}", "UTS_": "f", "\\Y]^": "i"}
encoding = {k: v * 4 for k, v in encoding.items()}
print(" ".join(encoding.get(f, f) for f in frames))

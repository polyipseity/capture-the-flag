import numpy
import pandas
import wave

with wave.open("message.wav") as message:
    number_of_frames = message.getnframes()
    audio = message.readframes(number_of_frames)

audio_i16 = numpy.frombuffer(audio, dtype=numpy.int16)
audio_f = audio_i16.astype(numpy.float32) / 2**15

last = 0.0
collapsed = [last]
for sample in audio_f:
    if last != sample:
        last = sample
        collapsed.append(sample)

max_pts = list[float]()
size = len(collapsed)
for idx, sample in enumerate(collapsed):
    if idx == 0 or idx == size - 1:
        continue
    if collapsed[idx - 1] < sample and sample > collapsed[idx + 1]:
        max_pts.append(sample)

data = "".join(str(int(pt >= 0.5)) for pt in max_pts)
print(data)

"""
last = data[0]
data2 = list[int]()
last_count = 1
for char in data:
    if last != char:
        data2.append(last_count)
        last_count = 0
        last = char
    last_count += 1
print(data2)
"""


def reverse_str(string: str):
    return "".join(reversed(string))


frame_size = 2
decoded = tuple(
    int(data[frame_size * idx : frame_size * idx + frame_size], 2) - 1
    for idx in range(len(data) // frame_size)
)

# 0, +3, +9, -13, -3, +7, +9, -14, firebird

print(decoded)
print(pandas.Series(decoded).value_counts())
print("".join(map(chr, decoded)))
decoded = "".join(map(lambda a: "0" if a == 0 else "1", decoded))

frame_size = 8
decoded2 = tuple(
    int(decoded[frame_size * idx : frame_size * idx + frame_size], 2)
    for idx in range(len(decoded) // frame_size)
)
print(decoded2)
print(pandas.Series(decoded2).value_counts())
print("".join(map(chr, decoded2)))

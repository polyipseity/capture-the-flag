from collections import Counter


with open("Shanghai_Teahouse.mid", "rb") as midi:
    track = midi.read()[0x1028F + 1 : -4]

track_iter = iter(track)
events = tuple(
    map(
        lambda event: {
            "time": event[0],
            "note": event[2],
            "velocity": event[3],
        },
        zip(*((track_iter,) * 4)),
    )
)
events[0]["time"] += (0x9D - 128) * 128
times = tuple(event["time"] for event in events)
counter = Counter(times)

print(times)
print(counter)

with open("decode.txt", "wt") as out:
    for offset in range(256):
        out.write("".join(chr((time + offset) % 256) for time in times))
        out.write("\n")
        out.write("=" * 256)
        out.write("\n")

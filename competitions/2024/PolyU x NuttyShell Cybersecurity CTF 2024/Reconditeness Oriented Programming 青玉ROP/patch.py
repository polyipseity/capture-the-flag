from pathlib import Path

original = Path("rop").read_bytes()
patch = Path("code.bin").read_bytes()
location = 0x401176 - 0x400000
end = 0x404D77 - 0x400000
size = end - location
patched = original[:location] + patch + b"\x00" * (size - len(patch)) + original[end:]
Path("rop_patched").write_bytes(patched)

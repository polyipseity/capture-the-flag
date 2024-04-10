from pathlib import Path


if __name__ == "__main__":
    rop = Path("rop").read_bytes()
    ret = bytes(byte ^ 42 for byte in rop)  # memfrob
    Path("rop_xor_42.bin").write_bytes(ret)
    idx = ret.find(b"That's the flag!")
    print(hex(0x401000 + idx))
    print(
        " ".join("%.2x" % (byte ^ 42,) for byte in b"That's the flag!")
    )  # 0x00000000004C55BD
    idx -= 229
    print(hex(0x401000 + idx))
    Path("rop_patched_xor_42.bin").write_bytes(
        rop[:idx] + ret[idx : idx + 246] + rop[idx + 246 :]
    )

from ctypes import c_uint64
from pathlib import Path
import re


def encode(input: c_uint64):
    rdi = c_uint64(input.value & (2**56 - 1))
    goals = re.compile(r"func(2|3)").finditer(Path("history_encode.txt").read_text())

    # init -> func3_2
    rcx, r8, r9 = c_uint64(0x25), rdi, c_uint64(0x1)
    first, dispatch = True, 3
    while True:
        if dispatch == 2:
            # func2
            r9, rdi, rsi = rdi, rcx, rcx
        elif dispatch == 2.2:
            rdi, rsi = rcx, rcx
        elif dispatch == 3:
            if not first:
                # func3 -> func3_2
                rcx, r8 = rdi, c_uint64(r8.value >> 1)
            first = False
            # func3_2
            if r8.value == 0:
                rdi = r9
                try:
                    dispatch = int(next(goals)[1])
                except StopIteration:
                    return rdi
                continue
            if (r8.value & 0x1) == 0:
                dispatch = 2.2
                continue
            rdi, rsi = r9, rcx
        else:
            raise NotImplementedError()
        # common_func
        lower = rdi.value * rsi.value
        upper, lower = c_uint64(lower >> 64), c_uint64(lower & (2**64 - 1))
        rdi = c_uint64(
            ((lower.value >> 61) | (upper.value << 3)) + (lower.value & (2**61 - 1))
        )
        rdi = c_uint64(
            (rdi.value - 0x1FFFFFFFFFFFFFFF)
            if rdi.value >= 0x1FFFFFFFFFFFFFFF
            else rdi.value
        )
        try:
            dispatch = int(next(goals)[1])
        except StopIteration:
            return rdi


if __name__ == "__main__":
    # 0x6867666564636261: 0x1bb0e29abc74a9f9
    print(hex(encode(c_uint64(0x6867666564636261)).value))
    print(hex(encode(c_uint64(int.from_bytes(reversed(b"gigem{ab")))).value))
    for idx in range(65536):
        ret = int.from_bytes(reversed(b"gigem{")) + idx << 48
        if hex(encode(c_uint64(ret)).value) == "0x144e5d522649ff85":
            print(ret)
            break
    # target: 0x144e5d522649ff85

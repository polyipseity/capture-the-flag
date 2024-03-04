from pathlib import Path

from iced_x86 import BlockEncoder, Decoder, Encoder, Instruction, Mnemonic

instructions = tuple(
    int(line[2:], 16) for line in Path("instructions.txt").read_text().splitlines()
)

with open("rop", "rb") as exe:
    exe_data = exe.read()
    chunks = tuple(
        (ins, exe_data[ins - 0x400000 : ins - 0x400000 + 64]) for ins in instructions
    )

real_instructions = list[Instruction]()
last_ret = None
for rip, data in chunks:
    decoder = Decoder(64, data, ip=rip)
    for ins in decoder:
        if ins.mnemonic == Mnemonic.RET:
            last_ret = ins
            break
        real_instructions.append(ins)
assert last_ret is not None
real_instructions.append(last_ret)

encoder = BlockEncoder(64)
encoder.add_many(real_instructions)
Path("code.txt").write_text("\n".join(map(str, real_instructions)))
Path("code.bin").write_bytes(encoder.encode(0x0000000000401176))

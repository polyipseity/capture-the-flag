from enum import StrEnum, auto
from socket import AF_INET, socket
from ssl import SOCK_STREAM
from typing import Collection

RECEIVE_SIZE = 65536
ALPHABET = "abcdefghijklmnopqrstuvwxyz{}_"


class RunResult(StrEnum):
    TRUE = auto()
    FALSE = auto()
    TRAPPED = auto()


def recv_and_send(socket: socket, text: str):
    ret = socket.recv(RECEIVE_SIZE).decode("utf-8")
    print(ret, end="")
    print(text)
    socket.send(f"{text}\n".encode())
    return ret


def run(states: int, final_states: Collection[int], transitions: Collection[str]):
    s = socket(AF_INET, SOCK_STREAM)
    try:
        s.connect(("dyn.ctf.pearlctf.in", 30018))
        recv_and_send(s, str(states))
        recv_and_send(s, " ".join(map(str, final_states)))
        recv_and_send(s, str(len(transitions)))
        for transition in transitions:
            recv_and_send(s, transition)
        ret = s.recv(RECEIVE_SIZE).decode("utf-8")
        print(ret)
        ret = ret.strip()
        return (
            RunResult.TRUE
            if ret == "1"
            else RunResult.FALSE if ret == "0" else RunResult.TRAPPED
        )
    finally:
        s.close()


"""
attack
"""


def find_length():
    length = 0
    while True:
        length += 1
        if (
            run(
                length + 1,
                (length,),
                tuple(f"{idx} @ {idx + 1}" for idx in range(length))
                + (f"{length} @ {length}",),
            )
            != RunResult.TRUE
        ):
            length -= 1
            return length


def find_next_char(skip: int, hints: str = ""):
    alphabet = f"{hints}{''.join(sorted(frozenset(ALPHABET) - frozenset(hints)))}"
    for char in alphabet:
        if (
            run(
                skip + 2,
                (skip + 1,),
                tuple(f"{idx} @ {idx + 1}" for idx in range(skip))
                + (f"{skip} ~{char} {skip + 1}", f"{skip + 1} @ {skip + 1}"),
            )
            == RunResult.TRAPPED
        ):
            return char
    raise RuntimeError()


if __name__ == "__main__":
    length = 0
    if length <= 0:
        length = find_length()
    print(f"Length is {length}")

    flag = ""
    if not flag:
        hints = "pearl{"
        for idx in range(length):
            ret = find_next_char(idx, hints[idx : idx + 1])
            print(f"Next char is {ret}")
            flag += ret
    print(f"Flag is {flag}")

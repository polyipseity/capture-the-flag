import sympy
from typing import Sequence


def calc(answer: Sequence[int], indices: str, ops: str):
    indices2 = list(map(int, indices))
    mat_row = [0] * 10
    idx = -1
    ret = answer[indices2[(idx := idx + 1)]]
    mat_row[indices2[idx]] += 1
    for op in ops:
        if op == "+":
            ret += answer[indices2[(idx := idx + 1)]]
            mat_row[indices2[idx]] += 1
        elif op == "-":
            ret -= answer[indices2[(idx := idx + 1)]]
            mat_row[indices2[idx]] -= 1
        else:
            raise ValueError(ops)
    print(tuple(mat_row))
    return ret


def solveme(ans: str):
    answer = list(map(ord, list(ans.strip())))
    if len(answer) != 10:
        raise ValueError(ans)
    if (
        calc(answer, "6785", "++-") != 190
        or calc(answer, "6552", "++-") != 202
        or calc(answer, "9325", "+++") != 433
        or calc(answer, "7003", "+-+") != 237
        or calc(answer, "1954", "--+") != -50
        or calc(answer, "2311", "-+-") != -6
        or calc(answer, "8765", "--+") != -88
        or calc(answer, "0853", "+--") != -117
        or calc(answer, "5682", "+++") != 385
        or calc(answer, "5459", "--+") != 4
        or calc(answer, "2950", "-+-") != 63
        or calc(answer, "2549", "-+-") != 13
        or calc(answer, "8376", "++-") != 167
        or calc(answer, "6505", "---") != -126
        or calc(answer, "2564", "---") != -199
    ):
        raise ValueError(ans)
    print("Correct!")


def solve():
    x0, x1, x2, x3, x4, x5, x6, x7, x8, x9 = sympy.symbols(
        list(f"x{idx}" for idx in range(10))
    )
    return sympy.solve_linear_system(
        sympy.Matrix(
            (
                (0, 0, 0, 0, 0, -1, 1, 1, 1, 0, 190),
                (0, 0, -1, 0, 0, 2, 1, 0, 0, 0, 202),
                (0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 433),
                (0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 237),
                (0, 1, 0, 0, 1, -1, 0, 0, 0, -1, -50),
                (0, 0, 1, -1, 0, 0, 0, 0, 0, 0, -6),
                (0, 0, 0, 0, 0, 1, -1, -1, 1, 0, -88),
                (1, 0, 0, -1, 0, -1, 0, 0, 1, 0, -117),
                (0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 385),
                (0, 0, 0, 0, -1, 0, 0, 0, 0, 1, 4),
                (-1, 0, 1, 0, 0, 1, 0, 0, 0, -1, 63),
                (0, 0, 1, 0, 1, -1, 0, 0, 0, -1, 13),
                (0, 0, 0, 1, 0, 0, -1, 1, 1, 0, 167),
                (-1, 0, 0, 0, 0, -2, 1, 0, 0, 0, -126),
                (0, 0, 1, 0, -1, -1, -1, 0, 0, 0, -199),
            )
        ),
        x0,
        x1,
        x2,
        x3,
        x4,
        x5,
        x6,
        x7,
        x8,
        x9,
    )


if __name__ == "__main__":
    solution = [51, 52, 115, 121, 95, 98, 121, 116, 51, 99]
    sol_str = bytes(solution).decode()
    print(sol_str)
    solveme(sol_str)

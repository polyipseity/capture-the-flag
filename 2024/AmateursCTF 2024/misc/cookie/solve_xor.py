from pathlib import Path
import sympy
from sympy.polys.matrices import DomainMatrix
from torch import mm
from tqdm.auto import tqdm


if __name__ == "__main__":
    xor = Path("xor.txt").read_text()
    xors = xor.splitlines()
    width = len(xors[0])
    assert all(len(xor) == width for xor in xors)
    symbols = sympy.symbols(
        list(f"x{idx}" for idx in range(width // 2) if idx % 8 != 0)
    )
    equations = list[list[int]]()
    results = list[int]()
    with tqdm(total=len(xors) * width // 2) as prog:
        for line in xors:
            count = 0
            equation = list[int]()
            variables = []
            for idx in range(width // 2):
                first, second = line[idx * 2 : idx * 2 + 2]
                if first == "1":
                    count += 1
                if idx % 8 != 0:
                    equation.append(1 if second == "X" else 0)
                prog.update()
            equations.append(equation)
            results.append(1 if count % 2 == 0 else 0)

    # https://github.com/sympy/sympy/issues/19243#issuecomment-1326792289
    m = sympy.Matrix(equations)
    b = sympy.Matrix(results)
    K = sympy.GF(2, symmetric=False)
    mm = DomainMatrix.from_Matrix(m).convert_to(K)
    bm = DomainMatrix.from_Matrix(b).convert_to(K)
    print(mm.lu_solve(bm).to_Matrix().T)

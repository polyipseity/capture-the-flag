import random, base64

funs = [
    lambda x, y: x,
    lambda x, y: x + y,
    lambda x, y: x - y,
    lambda x, y: x * y,
    lambda x, y: x // y,
    lambda x, y: x % y,
    lambda x, y: x & y,
    lambda x, y: x | y,
    lambda x, y: x ^ y,
    lambda x, y: (x << y if y > 0 else x >> -y),
    lambda x, y: x < y,
    lambda x, y: x == y,
    lambda x, y: x > y,
    lambda x, y: x <= y,
    lambda x, y: x >= y,
    lambda x, y: x != y,
    # there're more functions for use in reverse chall only, not listed here - but most of them are bivariate functions too
]


def run(code, stack):
    _code = list(code[::-1])
    _stack = stack[::-1]
    while len(_code) > 0:
        match _code.pop():
            case 255:
                stack.append(_code.pop() * 256 + _code.pop())
            case 254:
                stack.append(_code.pop())
            case 253:
                stack[-1], stack[-2] = stack[-2], stack[-1]
            case 252 | 251 | 250 | 249 as k:
                stack.append(stack[k - 253])
            case 248:
                print(tuple(map(hex, stack)))
            case _ as k:
                x = stack.pop()
                y = stack.pop()
                res = int(funs[k](y, x))
                if res.bit_length() > 100000:
                    raise OverflowError
                stack.append(res)
    return stack[::-1]


code = base64.b64decode(input("Your Stack Machine code: "))
assert len(code) <= 5000

for i in range(10):
    orig_nums = [
        random.randint(32, 127) for i in range(random.randint(20, 30))
    ]  # was [random.randint(32,127) for i in range(30)]
    sorted_nums = sorted(orig_nums)
    orig_num = int.from_bytes(bytes(orig_nums), "big")
    sorted_num = int.from_bytes(bytes(sorted_nums), "big")
    print(f"                {hex(orig_num)=}")
    print(f"              {hex(sorted_num)=}")
    print(f"{hex(run(code, [orig_num])[0])=}")
    assert run(code, [orig_num])[0] == sorted_num

print("OK, you will get flag")

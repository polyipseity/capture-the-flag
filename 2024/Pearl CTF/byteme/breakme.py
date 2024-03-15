def breakme(chain: str):
    best = [117, 84, 87, 108, 59, 85, 66, 71, 71, 30, 16]
    mod = list[int]()
    plier = 69
    for i in range(len(chain)):
        mod.append(plier ^ ord(chain[i]))
        plier = ord(chain[i])
    if mod != best:
        return
    print("Correct!")


def reverse():
    mod = [117, 84, 87, 108, 59, 85, 66, 71, 71, 30, 16]
    chain = list[int]()
    plier = 69
    for i in range(len(mod)):
        plier ^= mod[i]
        chain.append(plier)
    return chain


if __name__ == "__main__":
    chain = bytes(reverse()).decode()
    print(chain)
    breakme(chain)

from pyth_primes import *

factors = (
    3595649,
    4022869,
    4112629,
    5324453,
    7676377,
    7780589,
    8021257,
    8083961,
    8522509,
    8551537,
    8726801,
    9041189,
    9397301,
    9525757,
    9801269,
    10340017,
    10367933,
    10967633,
    13950301,
    14011601,
    14164217,
    15460469,
    15674053,
    16299013,
    16422761,
    16901737,
    17772257,
    17953301,
    18078149,
    18910897,
    19118173,
    19143401,
    19417817,
    19681301,
    20148613,
    20368837,
    20456309,
    20548961,
    20917873,
    21026129,
    22049821,
    23785477,
    24326521,
    24673933,
    27453077,
    29932421,
    33819397,
    36418873,
    36848869,
    36921457,
    37174957,
    37536497,
    37955321,
    38475181,
    39218969,
    39311521,
    39339301,
    39489209,
    39727661,
    39867617,
    40147249,
    40242313,
    43982329,
    44296129,
    46430029,
    46529297,
    49774913,
    50215393,
    50235301,
    52525589,
    53113369,
    56579917,
)

reversed = tuple(pyth_primes.index(a) + 1 for a in factors)
print(reversed)


def forward(string: bytes):
    for a in range(len(string) - 2):
        yield pyth_primes[string[a] * string[a + 1] * string[a + 2] - 1]


def get_missing_factors(string: bytes) -> set[int]:
    return set(factors) - set(forward(string))


def guess_next_char(string: bytes):
    guess = bytes(range(1, 256))
    missing = get_missing_factors(string)
    for a in guess:
        try:
            missing2 = get_missing_factors(string + bytes([a]))
            if len(missing2) < len(missing):
                print(f"possible: {chr(a)}")
        except IndexError:
            continue


# manual guessing required
# firebird{***REDACTED***}
# firebird{1940s_pr1m3_g3n3r47or_https://www.youtube.com/watch?v=j5s0h42GfvM}

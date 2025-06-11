from typing import List 
import math
from itertools import product


def main(Y: List[int]) -> int:
    E = [abs(v) for v in Y if (v < -72 or v>=48)]
    N = [v2*v2 + 2*v2 for v2 in Y if (v2 >= -65)]
    vi = [ eve*vivi for eve in E for vivi in N if eve < vivi]

    first = len(N)
    second = sum(vivi+ vi1 for vivi,vi1 in product(N, vi))
    return first + second


print(main({1, -30, -47, 82, 83, 53, -74, -73, 91, 28}))
print(main({-94, -55, 10, 78, 83, -43, -10, -98, 95}))

def main(hex_string):
    value = int(hex_string, 16)

    b1 = value & 0b1111111                    # биты 0–6
    b2 = (value >> 7) & 0b11                  # биты 7–8
    b3 = (value >> 9) & 0b111                 # биты 9–11
    b4 = (value >> 12) & 0b1                  # бит 12
    b5 = (value >> 13) & 0b11                 # биты 13–14
    b6 = (value >> 15) & 0b1111111            # биты 15–21

    return tuple(hex(x) for x in (b1, b2, b3, b4, b5, b6))
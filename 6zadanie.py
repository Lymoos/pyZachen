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

import time
import random

from collections import defaultdict
from typing import List


def main(nums: List[int]) -> bool:
    nums_freq = defaultdict()
    for num in nums:
        if num in nums_freq.keys():
            return True
        nums_freq[num] = 1
    return False


def main2(nums: List[int]) -> bool:
    listo = []
    for n in nums:
        if n in listo:
            return True
        listo.append(n)
    return False


if __name__ == "__main__":
    N = 1000_000

    rango = list(range(N))
    rango = [random.randint(1, 1_000) for _ in range(N)]

    s = time.time()
    # main(rango)
    print(time.time() - s)

    s = time.time()
    # main2(rango)
    print(time.time() - s)

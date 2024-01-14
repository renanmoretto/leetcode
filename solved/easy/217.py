import time

from collections import defaultdict
from typing import List


# def main(nums: List[int]) -> bool:
#     nums_freq = defaultdict()
#     for num in nums:
#         if num in nums_freq.keys():
#             return True
#         nums_freq[num] = 1
#     return False


def main(nums: List[int]) -> bool:
    listo = []
    for n in nums:
        if n in listo:
            return True
        listo.append(n)
    return False


if __name__ == "__main__":
    N = 1_000_000

    rango = list(range(N))
    main(rango)

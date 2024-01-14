import math

from functools import reduce
from operator import mul

MOD = 10**9 + 7


def calc_word_permutation(word: str) -> int:
    word_size = len(word)

    r = [word.count(s) for s in set(word) if word.count(s) > 1]
    denominator = math.prod([math.factorial(n) for n in r])

    word_permutations = math.factorial(word_size) / denominator
    return int(word_permutations)


def main(s: str) -> int:
    words = [w for w in s.split(" ")]
    total_vars = [calc_word_permutation(word) for word in words]
    return reduce(mul, total_vars)


word = "ukgqajqsuset"  # 11880, 2!*2!*2!
print(main(word))

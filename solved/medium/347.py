from collections import Counter


def main(nums: list[int], k: int) -> list[int]:
    return list(map(lambda x: x[0], Counter(nums).most_common(k)))


if __name__ == '__main__':
    inp = [1, 1, 1, 2, 2, 3, 5, 5, 5, 5]
    k = 3
    r = main(inp, k)
    print(r)

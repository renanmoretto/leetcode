def main(nums: list[int], target: int) -> list[int]:
    for i1, n1 in enumerate(nums):
        for i2, n2 in enumerate(nums):
            if i2 == i1:
                continue
            if n1 + n2 == target:
                return [i1, i2]


if __name__ == "__main__":
    r = main([2, 7, 11, 15], 26)
    print(r)

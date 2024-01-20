# ----------------------------------- O(n²) ---------------------------------- #

import math


def s1(nums: list[int]) -> list[int]:
    prods = []
    for i1, _ in enumerate(nums):
        prod = 1
        for i2, n2 in enumerate(nums):
            if i1 == i2:
                continue
            prod *= n2
        prods.append(prod)
    return prods


def s2(nums: list[int]) -> list[int]:
    prods = []
    for i in range(len(nums)):
        nums_ex_i = nums.copy()
        nums_ex_i.pop(i)
        prods.append(math.prod(nums_ex_i))
    return prods


def s3(nums: list[int]) -> list[int]:
    return [(math.prod(nums[:i]) * math.prod(nums[i + 1 :])) for i in range(len(nums))]


# --------------------------- O(n) Time, O(n) Space -------------------------- #
def solution_without_division(nums: list[int]) -> list[int]:
    left = [1]

    for i in range(1, len(nums)):
        left.append(left[i - 1] * nums[i - 1])

    right = [1]
    nums_rev = nums[::-1]
    for i in range(1, len(nums_rev)):
        right.append(right[i - 1] * nums_rev[i - 1])
    right = right[::-1]

    return [left[i] * right[i] for i in range(len(nums))]


# -------------------------------- O(n) Space -------------------------------- #


def solution_with_division_onspace(nums: list[int]) -> list[int]:
    zero_cnt = nums.count(0)

    if zero_cnt > 1:
        return [0] * len(nums)

    prod = 1
    for n in nums:
        if n:
            prod *= n

    ans = []
    for n in nums:
        if zero_cnt:
            if n:
                r = 0
            else:
                r = prod
        else:
            r = int(prod / n)
        ans.append(r)

    return ans


# -------------------------------- O(1) Space -------------------------------- #
def solution_with_division_o1space(nums: list[int]) -> list[int]:
    zero_cnt = nums.count(0)

    if zero_cnt > 1:
        return [0] * len(nums)

    prod = 1
    for n in nums:
        if n:
            prod *= n

    for i, n in enumerate(nums):
        if zero_cnt:
            # If bool(n) is True (i.e. n > 0) then 0 must be outside, so prod ex n = 0.
            # If bool(n) is False then the prod ex n must be the total prod. Because n is 0.
            nums[i] = 0 if n else prod
        else:
            nums[i] = int(prod / n)

    return nums


if __name__ == "__main__":
    inp = [1, 2, 3, 4]
    inp = [-1, 1, 0, -3, 3]
    r = solution_with_division_o1space(inp)
    print(r)

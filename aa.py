def main(nums: list[int]) -> list[int]:
    left = [1]

    for i in range(1, len(nums)):
        left.append(left[i - 1] * nums[i - 1])

    right = [1]
    nums_rev = nums[::-1]
    for i in range(1, len(nums_rev)):
        right.append(right[i - 1] * nums_rev[i - 1])
    right = right[::-1]

    return [left[i] * right[i] for i in range(len(nums))]


inp = [-1, 1, 0, -3, 3]
inp = [1, 2, 3, 4]
r = main(inp)
print(r)
print(list(reversed(inp)))

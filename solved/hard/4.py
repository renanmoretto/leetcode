"""
4. Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
"""


# This is faster then using statistics median, idk why
def solution(nums1: list[int], nums2: list[int]) -> float:
    nums = sorted(nums1 + nums2)
    size = len(nums)
    return nums[size // 2] if size % 2 else (nums[size // 2 - 1] + nums[size // 2]) / 2


from statistics import median


def solution2(nums1: list[int], nums2: list[int]) -> float:
    return median(sorted(nums1 + nums2))


if __name__ == '__main__':
    nums1 = [1, 2]
    nums2 = [3, 4]
    r = solution(nums1, nums2)
    print(r)

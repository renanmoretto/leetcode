"""
4. Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
"""


def solution(nums1: list[int], nums2: list[int]) -> float:
    nums = nums1 + nums2
    nums.sort()

    size = len(nums)
    if size % 2 == 0:
        n1 = nums[size // 2 - 1]
        n2 = nums[size // 2]
        return (n1 + n2) / 2
    return nums[size // 2]


if __name__ == '__main__':
    nums1 = [1, 2]
    nums2 = [3, 4]
    r = solution(nums1, nums2)
    print(r)

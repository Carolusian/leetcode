"""
4. Median of Two Sorted Arrays

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""
from statistics import median


def findMedianSortedArrays(nums1, nums2) -> float:
    length = len(nums1) + len(nums2)
    numbers = [None] * length

    i, j = len(nums1) - 1, len(nums2) - 1
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            numbers[i + j + 1] = nums1[i]
            i -= 1
        else:
            numbers[i + j + 1] = nums2[j]
            j -= 1

    while i >= 0:
        numbers[i] = nums1[i]
        i -= 1

    while j >= 0:
        numbers[j] = nums2[j]
        j -= 1

    return median(numbers)


print(findMedianSortedArrays([1, 3], [2]))
print(findMedianSortedArrays([1, 2], [3, 4]))


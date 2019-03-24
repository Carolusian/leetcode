"""
1020. Partition Array Into Three Parts With Equal Sum

Given an array A of integers, return true if and only if we can partition the array into three non-empty parts with equal sums.

Formally, we can partition the array if we can find indexes i+1 < j with (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1])


Example 1:

Input: [0,2,1,-6,6,-7,9,1,2,0,1]
Output: true
Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
Example 2:

Input: [0,2,1,-6,6,7,9,-1,2,0,1]
Output: false
Example 3:

Input: [3,3,6,5,-2,2,5,1,-9,4]
Output: true
Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
 

Note:

3 <= A.length <= 50000
-10000 <= A[i] <= 10000
"""


def canThreePartsEqualSum(A) -> bool:
    the_sum = 0
    i, j = -1, -1

    # Find entire sum of the array.
    total = sum(A)
    if(total % 3 != 0):
        return False

    sum1 = total / 3
    sum2 = 2 * sum1
    for ind, val in enumerate(A):
        the_sum += val
        if (the_sum == sum1 and i == -1):
            i = ind
        elif(the_sum == sum2 and i >= 0 and j == -1):
            j = ind

    if (i != -1 and j != -1):
        return True
    return False


def canThreePartsEqualSum2(A) -> bool:
    for i, val in enumerate(A):
        for j, val in enumerate(A[i:]):
            p1, p2, p3 = A[:i], A[i:i + j], A[i + j:]
            if len(p1) == 0 or len(p2) == 0 or len(p3) == 0:
                continue
            sum1, sum2, sum3 = sum(p1), sum(p2), sum(p3)
            if sum1 == sum2 and sum1 == sum3:
                print(p1, p2, p3)
                return True
    return False


# print(canThreePartsEqualSum([0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]))
# print(canThreePartsEqualSum([0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1]))
# print(canThreePartsEqualSum([3, 3, 6, 5, -2, 2, 5, 1, -9, 4]))
# print(canThreePartsEqualSum([6, 1, 1, 13, -1, 0, -10, 20]))
# print(canThreePartsEqualSum([29, 31, 27, -10, -67, 22, 15, -1, -16, -29, 59, -18, 48]))
print(canThreePartsEqualSum([12, -4, 16, -5, 9, -3, 3, 8, 0]))

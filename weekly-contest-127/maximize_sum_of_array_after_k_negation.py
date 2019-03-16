"""
1005. Maximize Sum Of Array After K Negations
Given an array A of integers, we must modify the array in the following way: we choose an i and replace A[i] with -A[i], and we repeat this process K times in total.  (We may choose the same index i multiple times.)

Return the largest possible sum of the array after modifying it in this way.

 

Example 1:

Input: A = [4,2,3], K = 1
Output: 5
Explanation: Choose indices (1,) and A becomes [4,-2,3].
Example 2:

Input: A = [3,-1,0,2], K = 3
Output: 6
Explanation: Choose indices (1, 2, 2) and A becomes [3,1,0,2].
Example 3:

Input: A = [2,-3,-1,5,-4], K = 2
Output: 13
Explanation: Choose indices (1, 4) and A becomes [2,3,-1,5,4].
 

Note:

1 <= A.length <= 10000
1 <= K <= 10000
-100 <= A[i] <= 100
"""
def largestSumAfterKNegations(A, K):
    sorted_a = sorted(A)

    i = 0
    quota = K

    # try best to change all to positive
    negatives = [i for i in sorted_a if i <= 0]
    len_n = len(negatives)
    if len_n > 0:
        while i < len_n and quota > 0:
            if sorted_a[i] < 0:
                sorted_a[i] = -sorted_a[i]
                quota -= 1
                i += 1
            else:
                quota = 0
                break

    # try best to maintain positive integers 
    sorted_a = sorted(sorted_a)
    quota = quota % 2
    if quota == 1:
        sorted_a[0] = -sorted_a[0]
        quota -= 1
    return sum(sorted_a)
    
    # for i in range(K):
    #     sorted_a[i] = -sorted_a[i]
    # return sum(sorted_a)

print(largestSumAfterKNegations([4, 2, 3], 1))
print(largestSumAfterKNegations([3, -1, 0, 2], 3))
print(largestSumAfterKNegations([2, -3, -1, 5, -4], 2))





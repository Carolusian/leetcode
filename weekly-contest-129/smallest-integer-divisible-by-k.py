"""
1022. Smallest Integer Divisible by K

Given a positive integer K, you need find the smallest positive integer N such that N is divisible by K, and N only contains the digit 1.

Return the length of N.  If there is no such N, return -1.


Example 1:

Input: 1
Output: 1
Explanation: The smallest answer is N = 1, which has length 1.
Example 2:

Input: 2
Output: -1
Explanation: There is no such positive integer N divisible by 2.
Example 3:

Input: 3
Output: 3
Explanation: The smallest answer is N = 111, which has length 3.
 

Note:

1 <= K <= 10^5
"""


def smallestRepunitDivByK(K: int) -> int:
    """
    the following shows that the last number of K must be in (1, 3, 7, 9)

    for i in range(1, 8):
        n = int('1' * i)
        print(n)
        for k in range(1, n):
            if (n % k == 0):
                print(k)
        print("===")
    """
    if K % 10 not in (1, 3, 7, 9):
        return -1

    remind, reminders = 0, set()
    for l in range(1, K + 1):
        remind = (10 * remind + 1) % K
        if remind == 0: 
            return l
        if remind in reminders: 
            # if the reminders are in repeatable pattern, then, it is not divisible
            return -1
        reminders.add(remind)
    return -1


# print(smallestRepunitDivByK(1))
# print(smallestRepunitDivByK(2))
# print(smallestRepunitDivByK(3))
# print(smallestRepunitDivByK(9))
print(smallestRepunitDivByK(19927))
# print(smallestRepunitDivByK(5367))

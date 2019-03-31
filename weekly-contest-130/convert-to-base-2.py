"""
1028. Convert to Base -2

Given a number N, return a string consisting of "0"s and "1"s that represents its value in base -2 (negative two).

The returned string must have no leading zeroes, unless the string is "0".

Example 1:

Input: 2
Output: "110"
Explantion: (-2) ^ 2 + (-2) ^ 1 = 2
Example 2:

Input: 3
Output: "111"
Explantion: (-2) ^ 2 + (-2) ^ 1 + (-2) ^ 0 = 3
Example 3:

Input: 4
Output: "100"
Explantion: (-2) ^ 2 = 4


Note:

0 <= N <= 10^9
"""


def baseNeg2(N: int) -> str:
    if N == 0:
        return "0"

    x, digits = N, ""
    while x != 0:
        x, remainder = divmod(x, -2)
        if remainder < 0:
            x, remainder = x + 1, remainder + 2
        digits = str(remainder) + digits
    return digits

# print(baseNeg2(2))
print(baseNeg2(3))
# print(baseNeg2(4))

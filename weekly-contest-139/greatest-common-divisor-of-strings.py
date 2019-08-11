"""
1071. Greatest Common Divisor of Strings

For strings S and T, we say "T divides S" if and only if S = T + ... + T  (T concatenated with itself 1 or more times)

Return the largest string X such that X divides str1 and X divides str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
 

Note:

1 <= str1.length <= 1000
1 <= str2.length <= 1000
str1[i] and str2[i] are English uppercase letters.
"""

import os
import math

def gcdOfStrings(str1: str, str2: str) -> str:
    common_str = os.path.commonprefix([str1, str2])
    len1, len2 = len(str1), len(str2)

    if not common_str:
        return ""
    
    len_gcd = math.gcd(len1, len2)
    return str1[:len_gcd]


if __name__ == '__main__':
    print(gcdOfStrings('ABCABC', 'ABC'))
    print(gcdOfStrings('ABABAB', 'ABAB'))
    print(gcdOfStrings('LEET', 'CODE'))

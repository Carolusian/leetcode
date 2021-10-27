# String Rotation: Assume you have a method isSubstring which checks if one word is a substring
# of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one
# call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat").
# Hints: #34, #88, # 7 04
#
# Solution 1: find where is the cut point O(N)
# Solution 2: check if s2 is a substring of s1s1, in this example s1s1 is "waterbottlewaterbottle" O(A+B)

import unittest
import time


def string_rotation(s1, s2) -> bool:
    if len(s1) != len(s2):
        return False
    start = time.time()
    for i in range(len(s1)):
        if s1[i:] + s1[:i] == s2:
            return True
    print(time.time() - start)
    return False


def string_rotation_sub(s1, s2) -> bool:
    if len(s1) != len(s2):
        return False
    start = time.time()
    res = s2 in s1 + s1
    print(time.time() - start)
    return res


test_cases = (
    ("waterbottle", "erbottlewat", True),
    ("waterbottle", "erbottliwat", False),
)

test_funcs = (string_rotation, string_rotation_sub)


class Test(unittest.TestCase):
    def test_string_rotation(self):
        for test_case in test_cases:
            s1, s2, expect = test_case
            for func in test_funcs:
                assert func(s1, s2) == expect


if __name__ == "__main__":
    unittest.main()

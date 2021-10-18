# given two strings, write a method to decide if one is a permutation of the other

import unittest
from collections import Counter
from itertools import permutations


class Test(unittest.TestCase):
    def test_check_perm(self):
        s1, s2 = "abc", "cba"
        self.assertTrue(check_permutation(s1, s2))

        s1, s2 = "abcdjfklsjfsdkl", "fkdsjfwdofjdskfdj"
        self.assertFalse(check_permutation(s1, s2))

        s1, s2 = "abccd", "bccda"
        self.assertTrue(check_permutation(s1, s2))

        s1 = "ewofdsggk"
        for p in permutations(s1):
            s2 = "".join(p)
            self.assertTrue(check_permutation(s1, s2))

        s1, s2 = "hello", "ooleh"
        self.assertFalse(check_permutation(s1, s2))


def check_permutation(s1: str, s2: str) -> bool:
    # a string is a permutation of itself
    if s1 == s2: 
        return True
    # not a permutation is the length of two string are not equal
    if len(s1) != len(s2): 
        return False

    return Counter(s1) == Counter(s2)

# TODO: using list/array index to represent the character using ord


if __name__ == "__main__":
    unittest.main()


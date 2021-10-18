# given two strings, write a method to decide if one is a permutation of the other

import unittest
from collections import Counter
from itertools import permutations


class Test(unittest.TestCase):
    def test_check_perm(self):
        s1, s2 = "abc", "cba"
        self.assertTrue(check_perm(s1, s2))

        s1, s2 = "abcdjfklsjfsdkl", "fkdsjfwdofjdskfdj"
        self.assertFalse(check_perm(s1, s2))

        s1, s2 = "abccd", "bccda"
        self.assertTrue(check_perm(s1, s2))

        s1 = "ewofdsggk"
        for p in permutations(s1):
            s2 = "".join(p)
            self.assertTrue(check_perm(s1, s2))

        s1, s2 = "hello", "ooleh"
        self.assertFalse(check_perm(s1, s2))


def check_perm(s1: str, s2: str) -> bool:
    # a string is a permutation of itself
    if s1 == s2: 
        return True
    # not a permutation is the length of two string are not equal
    if len(s1) != len(s2): 
        return False

    ctr1 = Counter(s1)
    ctr2 = Counter(s2)

    all_chars = set(s1) | set(s2)
    try:
        for c in all_chars:
            if ctr1[c] != ctr2[c]:
                return False
    except:
        return False
    return True

if __name__ == "__main__":
    unittest.main()


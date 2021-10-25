# String Compression: Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z).
#
# See also: leetcode string compression

import collections
import unittest


def string_compression(chars: list[str]) -> list[str]:
    """
    idea: 
    - iteratively append the characters and their count to the new array
    - since the original array have enough spare space after compressed
    - we just use the spare space as the new array
    ---
    the essential piece of code

    cnt = collections.Counter()
    last_char = ""

    for i, c in enumerate(chars):    
        cnt[c] += 1
        if last_char != c and last_char != "":    
            del cnt[last_char]
        last_char = c
    """
    if len(chars) == 1:
        return chars

    cnt = collections.Counter()
    last_char = ""
    cursor = 0

    for c in chars:
        cnt[c] += 1
        if last_char != c and last_char != "":
            chars[cursor] = last_char
            cursor += 1
            if cnt[last_char] > 1:
                for n in str(cnt[last_char]):
                    chars[cursor] = n
                    cursor += 1
            del cnt[last_char]
        last_char = c

    # move remaining item in counter to chars
    for k, v in cnt.items():
        chars[cursor] = k
        cursor += 1
        if v > 1:
            for n in str(v):
                chars[cursor] = n
                cursor += 1
    return chars[:cursor]


class Test(unittest.TestCase):
    test_cases = (
        (["a","a","b","b","c","c","c"], ["a","2","b","2","c","3"]), 
        (["a"], ["a"]), 
        (["a","b","b","b","b","b","b","b","b","b","b","b","b"], ["a","b","1","2"]),
        (["a","a","a","b","b","a","a"], ["a","3","b","2","a","2"]),
    )
    def test_string_compression(self):
        for test_case in self.test_cases:
            chars, expect = test_case
            assert string_compression(chars) == expect


if __name__ == "__main__":
    unittest.main()

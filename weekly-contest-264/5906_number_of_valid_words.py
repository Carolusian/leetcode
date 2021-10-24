# 5906. Number of Valid Words in a Sentence
# User Accepted:0
# User Tried:0
# Total Accepted:0
# Total Submissions:0
# Difficulty:Easy
# A sentence consists of lowercase letters ('a' to 'z'), digits ('0' to '9'), hyphens ('-'), punctuation marks ('!', '.', and ','), and spaces (' ') only. Each sentence can be broken down into one or more tokens separated by one or more spaces ' '.
#
# A token is a valid word if:
#
# It only contains lowercase letters, hyphens, and/or punctuation (no digits).
# There is at most one hyphen '-'. If present, it should be surrounded by lowercase characters ("a-b" is valid, but "-ab" and "ab-" are not valid).
# There is at most one punctuation mark. If present, it should be at the end of the token.
# Examples of valid words include "a-b.", "afad", "ba-c", "a!", and "!".
#
# Given a string sentence, return the number of valid words in sentence.
#
#
#
# Example 1:
#
# Input: sentence = "cat and  dog"
# Output: 3
# Explanation: The valid words in the sentence are "cat", "and", and "dog".
# Example 2:
#
# Input: sentence = "!this  1-s b8d!"
# Output: 0
# Explanation: There are no valid words in the sentence.
# "!this" is invalid because it starts with a punctuation mark.
# "1-s" and "b8d" are invalid because they contain digits.
# Example 3:
#
# Input: sentence = "alice and  bob are playing stone-game10"
# Output: 5
# Explanation: The valid words in the sentence are "alice", "and", "bob", "are", and "playing".
# "stone-game10" is invalid because it contains digits.
# Example 4:
#
# Input: sentence = "he bought 2 pencils, 3 erasers, and 1  pencil-sharpener."
# Output: 6
# Explanation: The valid words in the sentence are "he", "bought", "pencils,", "erasers,", "and", and "pencil-sharpener.".
#
#
# Constraints:
#
# 1 <= sentence.length <= 1000
# sentence only contains lowercase English letters, digits, ' ', '-', '!', '.', and ','.
# There will be at least 1 token.

import unittest
import re


def count_valid_words(sentence: str) -> int:
    words = sentence.split()
    res = []
    for word in words:
        matches = re.findall(r"^[a-z-]*[\!\.\,]?$", word)
        # the matches shall generate only 1
        if len(matches) != 1:
            continue

        # - must be in the middle
        if matches[0].startswith("-") or matches[0].endswith("-"):
            continue

        if len([c for c in matches[0] if c == "-"]) > 1:
            continue

        if len(re.findall(r"\-[\!\.\,]$", matches[0])) >= 1:
            continue

        res.append(matches[0])
    print(res)

    return len(res)


class Solution:
    def countValidWords(self, sentence: str) -> int:
        return count_valid_words(sentence)


class Test(unittest.TestCase):

    test_cases = (
        ("cat and  dog", 3),
        ("!this  1-s b8d!", 0),
        ("alice and  bob are playing stone-game10", 5),
        ("he bought 2 pencils, 3 erasers, and 1  pencil-sharpener.", 6),
        ("!", 1),
    )

    def test_count_valid_words(self):
        for test_case in self.test_cases:
            sentence, expect = test_case
            solution = Solution()
            assert solution.countValidWords(sentence) == expect


if __name__ == "__main__":
    # count_valid_words("cat and dog")
    # count_valid_words("!this  1-s b8d! ")
    # count_valid_words("alice and  bob are playing stone-game10")
    # count_valid_words("he bought 2 pencils, 3 erasers, and 1  pencil-sharpener.")
    # count_valid_words("!")
    # count_valid_words("a-b-c")
    # count_valid_words(
    #     " 62   nvtk0wr4f  8 qt3r! w1ph 1l ,e0d 0n 2v 7c.  n06huu2n9 s9   ui4 nsr!d7olr  q-, vqdo!btpmtmui.bb83lf g .!v9-lg 2fyoykex uy5a 8v whvu8 .y sc5 -0n4 zo pfgju 5u 4 3x,3!wl  fv4   s  aig cf j1 a i  8m5o1  !u n!.1tz87d3 .9    n a3  .xb1p9f  b1i a j8s2 cugf l494cx1! hisceovf3 8d93 sg 4r.f1z9w   4- cb r97jo hln3s h2 o .  8dx08as7l!mcmc isa49afk i1 fk,s e !1 ln rt2vhu 4ks4zq c w  o- 6  5!.n8ten0 6mk 2k2y3e335,yj  h p3 5 -0  5g1c  tr49, ,qp9 -v p  7p4v110926wwr h x wklq u zo 16. !8  u63n0c l3 yckifu 1cgz t.i   lh w xa l,jt   hpi ng-gvtk8 9 j u9qfcd!2  kyu42v dmv.cst6i5fo rxhw4wvp2 1 okc8!  z aribcam0  cp-zp,!e x  agj-gb3 !om3934 k vnuo056h g7 t-6j! 8w8fncebuj-lq    inzqhw v39,  f e 9. 50 , ru3r  mbuab  6  wz dw79.av2xp . gbmy gc s6pi pra4fo9fwq k   j-ppy -3vpf   o k4hy3 -!..5s ,2 k5 j p38dtd   !i   b!fgj,nx qgif "
    # )
    unittest.main()

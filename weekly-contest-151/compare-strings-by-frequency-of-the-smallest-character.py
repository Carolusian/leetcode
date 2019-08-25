"""
1170. Compare Strings by Frequency of the Smallest Character

Let's define a function f(s) over a non-empty string s, which calculates the frequency of the smallest character in s. For example, if s = "dcce" then f(s) = 2 because the smallest character is "c" and its frequency is 2.

Now, given string arrays queries and words, return an integer array answer, where each answer[i] is the number of words such that f(queries[i]) < f(W), where W is a word in words.

Example 1:

Input: queries = ["cbd"], words = ["zaaaz"]
Output: [1]
Explanation: On the first query we have f("cbd") = 1, f("zaaaz") = 3 so f("cbd") < f("zaaaz").
Example 2:

Input: queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
Output: [1,2]
Explanation: On the first query only f("bbb") < f("aaaa"). On the second query both f("aaa") and f("aaaa") are both > f("cc").
 

Constraints:

1 <= queries.length <= 2000
1 <= words.length <= 2000
1 <= queries[i].length, words[i].length <= 10
queries[i][j], words[i][j] are English lowercase letters.
"""
from typing import List


def numSmallerByFrequency(queries: List[str], words: List[str]) -> List[int]:
    ret = []
    queries = [sorted(q) for q in queries]
    queries = [q.count(q[0]) for q in queries]
    words = [sorted(w) for w in words]
    words = [w.count(w[0]) for w in words]

    for q in queries:
        num = 0
        for w in words:
            if w > q:
                num += 1
        ret.append(num)
    return ret


print(numSmallerByFrequency(["cbd"], ["zaaaz"]))
print(numSmallerByFrequency(["bbb","cc"], ["a","aa","aaa","aaaa"]))


"""
3. Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


def is_unique(s: str) -> bool:
    return len(set(s)) == len(s)


def lengthOfLongestSubstring(s: str) -> int:
    i, j, longest = 0, 0, 0

    while j <= len(s):
        substring = s[i:j]
        if is_unique(substring):
            longest = len(substring) if len(substring) > longest else longest
            j += 1
        else:
            i += 1
    return longest

print(lengthOfLongestSubstring('pwwkew'))
print(lengthOfLongestSubstring('au'))
print(lengthOfLongestSubstring(' '))


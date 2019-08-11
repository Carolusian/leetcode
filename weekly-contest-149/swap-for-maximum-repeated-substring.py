"""
1156. Swap For Longest Repeated Character Substring

Given a string text, we are allowed to swap two of the characters in the string. Find the length of the longest substring with repeated characters.

 

Example 1:

Input: text = "ababa"
Output: 3
Explanation: We can swap the first 'b' with the last 'a', or the last 'b' with the first 'a'. Then, the longest repeated character substring is "aaa", which its length is 3.
Example 2:

Input: text = "aaabaaa"
Output: 6
Explanation: Swap 'b' with the last 'a' (or the first 'a'), and we get longest repeated character substring "aaaaaa", which its length is 6.
Example 3:

Input: text = "aaabbaaa"
Output: 4
Example 4:

Input: text = "aaaaa"
Output: 5
Explanation: No need to swap, longest repeated character substring is "aaaaa", length is 5.
Example 5:

Input: text = "abcdef"
Output: 1
 

Constraints:

1 <= text.length <= 20000
text consist of lowercase English characters only.
"""

def maxRepeating(s: str) -> str:
    l = len(s) 
    count = 0
    index = 0
  
    # Find the maximum repeating  
    # character starting from str[i] 
    res = s[0] 
    for i in range(l): 
          
        cur_count = 1
        for j in range(i + 1, l): 
      
            if (s[i] != s[j]): 
                break
            cur_count += 1
  
        # Update result if required 
        if cur_count > count : 
            count = cur_count 
            res = s[i] 
            index = i
    return res 


def count(s: str, c: str) -> int:
    l = len(str) 
    count = 0
  
    # Find the maximum repeating  
    # character starting from str[i] 
    res = str[0] 
    for i in range(l): 
          
        cur_count = 1
        for j in range(i + 1, l): 
      
            if (str[i] != str[j]): 
                break
            cur_count += 1
  
        # Update result if required 
        if cur_count > count : 
            count = cur_count 
            res = str[i] 
    return res 
     

def maxRepOpt1(text: str) -> int:
    res = maxRepeating(text)
    return res 


print(maxRepOpt1('aaabbaaaa'))

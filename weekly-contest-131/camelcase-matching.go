/*
1023. Camelcase Matching

A query word matches a given pattern if we can insert lowercase letters to the pattern word so that it equals the query. (We may insert each character at any position, and may insert 0 characters.)

Given a list of queries, and a pattern, return an answer list of booleans, where answer[i] is true if and only if queries[i] matches the pattern.



Example 1:

Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB"
Output: [true,false,true,true,false]
Explanation:
"FooBar" can be generated like this "F" + "oo" + "B" + "ar".
"FootBall" can be generated like this "F" + "oot" + "B" + "all".
"FrameBuffer" can be generated like this "F" + "rame" + "B" + "uffer".
Example 2:

Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBa"
Output: [true,false,true,false,false]
Explanation:
"FooBar" can be generated like this "Fo" + "o" + "Ba" + "r".
"FootBall" can be generated like this "Fo" + "ot" + "Ba" + "ll".
Example 3:

Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBaT"
Output: [false,true,false,false,false]
Explanation:
"FooBarTest" can be generated like this "Fo" + "o" + "Ba" + "r" + "T" + "est".

Note:

1 <= queries.length <= 100
1 <= queries[i].length <= 100
1 <= pattern.length <= 100
All strings consists only of lower and upper case English letters.
*/

package main

import (
	"fmt"
	"unicode"
)

func hasUpper(s string) bool {
	if s == "" {
		return false
	}
	for _, c := range s {
		if unicode.IsUpper(c) {
			return true
		}
	}
	return false
}

func match(query string, pattern string) bool {
	if pattern == "" {
		return !hasUpper(query)
	}
	if len(query) < len(pattern) {
		return false
	}
	if query[0] == pattern[0] {
		// possible special case
		return match(query[1:], pattern[1:])

	} else {
		// otherwise must be false
		// unless the begining is arbitary lowercase character
		if hasUpper(string(query[0])) {
			return false
		} else {
			return match(query[1:], pattern)
		}
	}
}

func camelMatch(queries []string, pattern string) []bool {
	ret := make([]bool, len(queries))
	for i, s := range queries {
		ret[i] = match(s, pattern)
	}
	return ret
}

func main() {
	fmt.Println(match("FooBaTrT", "FB"))
	fmt.Println(camelMatch([]string{"FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"}, "FB"))
	fmt.Println(camelMatch([]string{"FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"}, "FoBa"))
}

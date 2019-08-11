/*
5083. Occurrences After Bigram

Given words first and second, consider occurrences in some text of the form "first second third", where second comes immediately after first, and third comes immediately after second.

For each such occurrence, add "third" to the answer, and return the answer.

Example 1:

Input: text = "alice is a good girl she is a good student", first = "a", second = "good"
Output: ["girl","student"]
Example 2:

Input: text = "we will we will rock you", first = "we", second = "will"
Output: ["we","rock"]


Note:

1 <= text.length <= 1000
text consists of space separated words, where each word consists of lowercase English letters.
1 <= first.length, second.length <= 10
first and second consist of lowercase English letters.
*/
package main

import (
	"fmt"
	"strings"
)

type Tuple struct {
	first, second string
}

func zip(first, second []string) ([]Tuple, error) {
	if len(first) != len(second) {
		return nil, fmt.Errorf("zip: arguments must of the same length.")
	}

	r := make([]Tuple, len(first), len(first))

	for i, e := range first {
		r[i] = Tuple{e, second[i]}
	}

	return r, nil
}

func findOcurrences(text string, first string, second string) []string {
	words := strings.Split(text, " ")
	x, y := words[:len(words)-1], words[1:]
	bigrams, _ := zip(x, y)
	l := len(bigrams)
	result := make([]string, 0)
	for i, e := range bigrams {
		if e.first == first && e.second == second && i < l-1 {
			result = append(result, bigrams[i+1].second)
		}
	}
	return result
}

func main() {
	fmt.Println(findOcurrences("alice is a good girl she is a good student", "a", "good"))
}

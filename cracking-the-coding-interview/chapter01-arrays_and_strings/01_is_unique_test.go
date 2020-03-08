package chapter01

import (
	"testing"
)

func TestIsUnique(t *testing.T) {
	testCases := map[string]bool{
		"a":           true,
		"ab":          true,
		"abcdefghijk": true,
		"abcxyz":      true,
		"aa":          false,
		"abcc":        false,
		"abccde":      false,
	}

	t.Run("using_map", func(t *testing.T) {
		for key, expected := range testCases {
			if actual := IsUnique(key); actual != expected {
				t.Errorf("Expected unqiue=%t for %s", expected, key)
			}
		}
	})
}

func IsUnique(s string) bool {
	set := make(map[rune]bool)

	for _, c := range s {
		if _, ok := set[c]; ok {
			return false
		}

		set[c] = true
	}
	return true
}

package main

import (
	"fmt"
)

func Solution(A int, B int) int {
	// write your code in Go 1.4
	n, count := A*B, 0

	for n > 0 {
		count += n & 1
		n = n >> 1
	}

	return count
}

func main() {
	fmt.Println(Solution(3, 7))
}

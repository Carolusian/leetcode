/*
1104. Path In Zigzag Labelled Binary Tree

In an infinite binary tree where every node has two children, the nodes are labelled in row order.

In the odd numbered rows (ie., the first, third, fifth,...), the labelling is left to right, while in the even numbered rows (second, fourth, sixth,...), the labelling is right to left.

{{Pic}}

Given the label of a node in this tree, return the labels in the path from the root of the tree to the node with that label.

Example 1:

Input: label = 14
Output: [1,3,4,14]
Example 2:

Input: label = 26
Output: [1,2,6,10,26]


Constraints:

1 <= label <= 10^6

Thoughts:
- You don't really need to construct a binary tree in ZigZag order
- One way is to caculate the number of nodes between two levels
*/
package main

import (
	"fmt"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func zigZagArray(last int) []int {
	r := make([]int, 0, last)
	return r
}

func pathInZigZagTree(label int) []int {
	r := make([]int, 0)
	return r
}

func main() {
	fmt.Println(pathInZigZagTree(14))
}

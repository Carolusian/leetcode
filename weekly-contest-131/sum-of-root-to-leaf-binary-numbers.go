/**
1022. Sum of Root To Leaf Binary Numbers

iven a binary tree, each node has value 0 or 1.  Each root-to-leaf path represents a binary number starting with the most significant bit.  For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.

For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.

Return the sum of these numbers.

Input: [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22

Note:

The number of nodes in the tree is between 1 and 1000.
node.val is 0 or 1.
The answer will not exceed 2^31 - 1.
*/

package main

import (
	"fmt"
	"math"
	"strconv"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// breadth first insert
// https://www.geeksforgeeks.org/insertion-in-a-binary-tree-in-level-order/
func (p *TreeNode) insert(v int) {
	tail := []*TreeNode{p}
	for len(tail) > 0 {
		head := tail[0]
		tail = tail[1:]
		if head.Left == nil {
			head.Left = &TreeNode{Val: v, Left: nil, Right: nil}
			break
		} else {
			tail = append(tail, head.Left)
		}

		if head.Right == nil {
			head.Right = &TreeNode{Val: v, Left: nil, Right: nil}
			break
		} else {
			tail = append(tail, head.Right)
		}
	}
}

func getPath(n *TreeNode, s string, allPath *[]string) {
	bin := s
	if n != nil {
		bin += strconv.Itoa(n.Val)
		if n.Left != nil {
			getPath(n.Left, bin, allPath)
		}

		if n.Right != nil {
			getPath(n.Right, bin, allPath)
		}

		if n.Left == nil && n.Right == nil {
			*allPath = append(*allPath, bin)
		}
	}
}

func sumRootToLeaf(root *TreeNode) int {
	paths := make([]string, 0)
	getPath(root, "", &paths)

	var sum int64 = 0
	for _, p := range paths {
		if i, err := strconv.ParseInt(p, 2, 0); err != nil {

		} else {
			sum += i
		}
	}
	return int(sum % int64(math.Pow(10, 9)+7))
}

func main() {
	l := []int{1, 0, 1, 0, 1, 0, 1}
	root := TreeNode{Val: l[0], Left: nil, Right: nil}
	for _, n := range l[1:] {
		root.insert(n)
	}
	// fmt.Println(&root)
	// fmt.Println(root.Left)
	// fmt.Println(root.Right)
	// fmt.Println(root.Left.Left)
	// fmt.Println(root.Left.Right)
	// fmt.Println(root.Right.Left)
	// fmt.Println(root.Right.Right)
	fmt.Println(sumRootToLeaf(&root))
}

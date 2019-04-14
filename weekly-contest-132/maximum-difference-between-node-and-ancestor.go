/*
1026. Maximum Difference Between Node and Ancestor

Given the root of a binary tree, find the maximum value V for which there exists different nodes A and B where V = |A.val - B.val| and A is an ancestor of B.

(A node A is an ancestor of B if either: any child of A is equal to B, or any child of A is an ancestor of B.)



Example 1:



Input: [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation:
We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.


Note:

The number of nodes in the tree is between 2 and 5000.
Each node will have value between 0 and 100000.
*/

package main

import (
	"fmt"
	"math"
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

func getPath(n *TreeNode, s []int, allPath *[][]int) {
	p := make([]int, 0)
	p = append(p, s...)
	if n != nil {
		if n.Val != 0 {
			p = append(p, n.Val)
		}
		if n.Left != nil {
			getPath(n.Left, p, allPath)
		}

		if n.Right != nil {
			getPath(n.Right, p, allPath)
		}

		*allPath = append(*allPath, p)
	}
}

func findLargestAbsoluteInPath(p []int) int {
	subpath := p
	ret := int(math.Abs(float64(subpath[0]) - float64(subpath[len(subpath)-1])))
	for {
		subpath = subpath[1:]
		if len(subpath) >= 2 {
			n := int(math.Abs(float64(subpath[0]) - float64(subpath[len(subpath)-1])))
			if n > ret {
				ret = n
			}
		} else {
			break
		}
	}
	return ret
}

func maxAncestorDiff(root *TreeNode) int {
	paths, ret := make([][]int, 0), 0
	getPath(root, []int{}, &paths)

	for _, p := range paths {
		if len(p) >= 2 {
			n := findLargestAbsoluteInPath(p)
			if n > ret {
				ret = n
			}
		}
	}
	return ret
}

func main() {
	l := []int{8, 3, 10, 1, 6, 0, 14, 0, 0, 4, 7, 13}
	root := TreeNode{Val: l[0], Left: nil, Right: nil}
	for _, n := range l[1:] {
		root.insert(n)
	}
	fmt.Println(maxAncestorDiff(&root))
}

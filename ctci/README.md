## VII. Technical Questions.

### What you need to know

- Core Data Structures
  ** Linked List
  ** Trees, Tries & Graphs
  ** Stacks & Queues
  ** Heaps
  ** Vectors/ArrayLists
  ** Hash Tables
- Algorithms
  ** BFS
  ** DFS
  ** Binary Search
  ** Merge Sort
  \*\* Quick Sort
- Concepts
  ** Bit Manipulation
  ** Memory (Stack vs Heap)
  ** Recursion
  ** Dynamic Programming
  \*\* Big O time & Space

### 5 Optimize & Solve Techniques

- Look for BUD (Bottleneck, Unnecessary work, Duplicated work)
- Do It Yourself
- Simplify and Generalize
- Base Case and Build
- Data Structure Brainstorm

## IX. Interview Questions

Important chapters: 1-5, 7-10

### Ch 1: Arrays and Strings

Hashtables, ArrayList & Resizable Arrays, StringBuilder

### Ch 2: Linked List

The "Runner" Technique, Recursive Problems (O(n) space where n is depth of recursive)

### Ch 3: Stacks and Queues

Stack: useful in recursive algorithms

#### Good stack problems on leetcode

- [Good stack problems by lee215](https://leetcode.com/problems/online-stock-span/discuss/168311/)
- [Sum of subarray minimums](https://leetcode.com/problems/sum-of-subarray-minimums/discuss/170750/)

### Ch 4: Trees and Graphs

- BFS:
  - typical scenario: find the minimum steps to transform from one state to another
  - example: https://leetcode.com/contest/weekly-contest-265/problems/minimum-operations-to-convert-number/
- DFS: implemented in recursion
- Topogical sort:
  - method 1: DFS + stack, stack is for cache and reverse the return, 3 status to detect circular
  - method 2: queueu, kahn's algorithm

### Ch 6: Math and Puzzles: NOT THAT Necessary

## Related leetcode questions

- https://leetcode.com/discuss/general-discussion/1152824/cracking-the-coding-interview-6th-edition-in-leetcode
- good dp question: https://leetcode.com/problems/network-delay-time/discuss/1614297/python-3-different-4-methods-no-explanation

## Tips

- Counter can be used to record number of operations, rather than really perform the operation, e.g. remove an element from container
- Dict can be used to record status, e.g. true|false; pending|inprogres|done

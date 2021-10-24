# 5908. Count Nodes With the Highest Score
# User Accepted:815
# User Tried:1080
# Total Accepted:829
# Total Submissions:1907
# Difficulty:Medium
# There is a binary tree rooted at 0 consisting of n nodes. The nodes are labeled from 0 to n - 1. You are given a 0-indexed integer array parents representing the tree, where parents[i] is the parent of node i. Since node 0 is the root, parents[0] == -1.
#
# Each node has a score. To find the score of a node, consider if the node and the edges connected to it were removed. The tree would become one or more non-empty subtrees. The size of a subtree is the number of the nodes in it. The score of the node is the product of the sizes of all those subtrees.
#
# Return the number of nodes that have the highest score.
#
#
#
# Example 1:
#
# example-1
# Input: parents = [-1,2,0,2,0]
# Output: 3
# Explanation:
# - The score of node 0 is: 3 * 1 = 3
# - The score of node 1 is: 4 = 4
# - The score of node 2 is: 1 * 1 * 2 = 2
# - The score of node 3 is: 4 = 4
# - The score of node 4 is: 4 = 4
# The highest score is 4, and three nodes (node 1, node 3, and node 4) have the highest score.
# Example 2:
#
# example-2
# Input: parents = [-1,2,0]
# Output: 2
# Explanation:
# - The score of node 0 is: 2 = 2
# - The score of node 1 is: 2 = 2
# - The score of node 2 is: 1 * 1 = 1
# The highest score is 2, and two nodes (node 0 and node 1) have the highest score.
#
#
# Constraints:
#
# n == parents.length
# 2 <= n <= 105
# parents[0] == -1
# 0 <= parents[i] <= n - 1 for i != 0
# parents represents a valid binary tree.

# -1, 2, 0, 2, 0
#   , 2, 0, 2, 0


from collections import defaultdict, Counter
import unittest
import functools
from typing import List, Dict


def get_parent(node: int, ptree: Dict[int, int]) -> int:
    """return the parent node"""
    return ptree[node]


def get_root_parent(node, ptree: Dict[int, int]) -> int:
    root = get_parent(node, ptree)
    result = root
    while root in ptree.keys():
        result = root
        root = get_parent(root, ptree)

    return result


# my solution
def count_highest_score_nodes(parents: List[int]) -> int:
    tree = defaultdict()
    for k, v in enumerate(parents):
        # consider replace it with a hashtable
        tree[k] = v

    # remove each node
    subtrees = []
    for node in tree.keys():
        subtree = dict(tree)
        del subtree[node]
        subtrees.append(subtree)

    # calc the scores of each subtree
    scores = {}
    for node, subtree in enumerate(subtrees):
        # find the size of each subtree
        parent_nodes = set(subtree.values())

        # every key which don't have parent is the root
        # use a dict to indict its nodes which doesn't have parent
        st = Counter()
        for p in parent_nodes:
            if not p in subtree.keys():
                # node and its parent_node
                for n, pn in subtree.items():
                    if p == pn:
                        st[n] += 1

        # count the elems of each sub tree
        for n, _ in subtree.items():
            root = get_root_parent(n, subtree)
            if root in st.keys():
                st[root] += 1

        score = functools.reduce(lambda x, y: x * y, st.values())
        scores[node] = score
    max_score = max(scores.values())
    num_nodes = len([s for s in scores.values() if s == max_score])
    return num_nodes


# better solution: https://leetcode.com/problems/count-nodes-with-the-highest-score/discuss/1537603/Python-3-or-Graph-DFS-Post-order-Traversal-O(N)-or-Explanation
# Explanation
# Intuition: Maximum product of 3 branches, need to know how many nodes in each branch, use DFS to start with
# Build graph
# Find left, right, up (number of nodes) for each node
    # left: use recursion
    # right: use recursion
    # up: n - 1 - left - right
# Calculate score store in a dictinary
# Return count of max key
# Time: O(n)

def count_highest_score_nodes_dfs(parents: List[int]) -> int:
    graph = defaultdict(list)
    for node, parent in enumerate(parents):
        graph[parent].append(node)
    
    n = len(parents)
    d = Counter()

    def count_nodes(node):
        p, s = 1, 0          # product and sum

        # if no children, just return 1 + 0
        for child in graph[node]:
            res = count_nodes(child)  

            # count from children
            s += res                  

            # product is asked from the question, so we need to save it
            p *= res   
        # the count is num(itself) + num(children)
        # the rational is to calculation the score with: left (num of node in separated subtree, since the current node removed) * right, then * n - 1 - s (total minus itself (removed), minus children (counted))
        p *= max(1, n - 1 - s)
        print(node, n, s, n - 1 - s)
        d[p] += 1
        return 1 + s

    count_nodes(0)
    return d[max(d.keys())]


class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        return count_highest_score_nodes(parents)


class Test(unittest.TestCase):
    test_cases = (([-1, 2, 0, 2, 0], 3), ([-1, 2, 0], 2), ([-1, 2, 0, 2, 0, 3, 4], 1), 
            ([-1,737,14,736,569,363,322,473,754,379,616,683,351,494,708,96,13,545,1,118,236,317,342,45,12,716,465,595,522,579,723,606,128,452,36,245,730,120,467,647,737,169,738,106,248,391,742,141,262,411,393,477,287,715,15,739,389,725,217,662,171,147,447,667,53,653,153,442,554,488,485,587,346,738,412,118,254,413,351,277,301,601,0,702,235,438,473,62,505,142,309,649,29,384,350,433,106,645,256,293,50,474,125,18,699,257,13,238,580,263,442,178,295,27,90,44,285,632,85,41,492,189,729,405,349,396,557,692,195,332,22,264,703,670,164,536,79,299,311,53,222,750,95,753,41,725,181,671,293,572,413,230,244,222,142,594,591,368,379,483,389,568,625,216,249,696,664,278,710,166,99,295,721,268,311,93,110,657,627,673,167,750,474,595,243,280,559,27,214,747,60,283,171,461,739,323,359,557,434,15,197,500,451,622,22,751,626,348,466,313,551,631,488,702,71,479,181,497,302,537,612,490,155,493,746,81,164,381,448,176,675,511,150,390,125,32,649,283,669,637,7,740,535,342,84,396,423,132,100,751,459,180,357,229,40,249,136,517,281,159,466,492,185,378,153,58,26,658,735,506,348,312,433,417,151,227,120,594,169,404,587,224,681,140,234,438,81,175,558,82,532,586,80,418,175,399,709,446,12,245,92,402,237,458,206,544,641,209,638,712,558,375,462,586,46,567,188,66,340,496,431,140,233,556,635,159,425,614,259,73,402,147,573,538,692,103,338,592,752,321,95,462,683,590,173,471,356,360,464,422,375,664,177,695,496,100,465,426,40,372,706,90,583,148,129,639,612,335,405,24,218,549,116,146,721,314,257,708,565,235,122,444,202,596,490,429,567,187,183,390,508,85,658,116,2,198,259,724,600,55,570,380,539,97,453,332,206,604,109,655,615,447,650,86,187,526,36,330,434,443,114,609,343,471,611,579,216,213,602,61,350,399,543,584,453,653,32,510,436,365,673,619,43,421,393,260,288,700,1,622,593,688,47,163,294,286,422,219,310,226,300,75,226,454,696,312,341,410,192,538,112,60,542,472,7,308,506,334,4,540,746,604,648,294,395,151,26,536,711,123,248,630,134,94,236,59,530,714,722,650,662,688,21,211,714,55,729,734,310,104,149,91,290,456,392,597,639,65,607,541,355,319,208,275,49,596,128,631,507,271,119,306,666,636,525,174,323,364,328,272,484,741,675,178,528,627,665,450,94,728,217,54,633,57,505,318,126,192,671,444,340,599,728,726,437,166,707,46,188,315,435,291,508,306,230,205,570,618,287,685,522,307,11,349,237,96,616,149,278,554,430,289,219,163,341,472,542,700,162,372,136,670,753,487,80,319,572,503,273,71,3,428,277,493,65,127,384,602,223,698,251,318,189,684,203,354,77,556,476,56,553,119,464,523,672,532,197,441,531,279,275,43,575,139,155,63,503,520,174,590,685,303,562,328,481,734,4,404,614,403,663,167,280,99,129,458,517,520,549,417,494,86,126,383,430,29,561,168,320,281,437,498,179,82,301,625,395,105,450,383,701,519,198,108,207,680,623,510,165,194,530,224,335,539,610,165,91,537,50,468,531,300,103,716,641,162,272,534,221,445,630,609,483,64,457,712,302,360,541,289,320,643,19,87,145,623,213,214,584,57,735,0,270,526,329,502,628,468,156,435,628,741,251,591,316], 1))

    def test_count_highest_score_nodes(self):
        for tc in self.test_cases:
            ptree, expect = tc
            sol = Solution()
            assert sol.countHighestScoreNodes(ptree) == expect

    def test_count_highest_score_nodes_dfs(self):
        for tc in self.test_cases:
            ptree, expect = tc
            assert count_highest_score_nodes_dfs(ptree) == expect


# count_highest_score_nodes([-1, 2, 0, 2, 0])
# count_highest_score_nodes([-1, 2, 0])
# count_highest_score_nodes([-1, 2, 0, 2, 0, 3, 4])
# count_highest_score_nodes_dfs([-1, 2, 0, 2, 0])
# tree = {}
# for k, v in enumerate([-1, 2, 0, 2, 0, 3, 4]):
#     # consider replace it with a hashtable
#     tree[k] = v

# # del tree[0]

# print(tree)
# print(get_root_parent(5, tree))
unittest.main()

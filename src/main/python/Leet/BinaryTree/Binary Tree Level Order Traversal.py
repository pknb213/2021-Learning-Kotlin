"""
Given the root of a binary tree, return the level order traversal of its nodes' values.
(i.e., from left to right, level by level).

Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: [[3],[9,20],[15,7]]
Example 2:
    Input: root = [1]
    Output: [[1]]
Example 3:
    Input: root = []
    Output: []

Constraints:
    The number of nodes in the tree is in the range [0, 2000].
    -1000 <= Node.val <= 1000
"""
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        pass


t5 = TreeNode(7, None, None)
t4 = TreeNode(15, None, None)
t3 = TreeNode(20, t4, t5)
t2 = TreeNode(9, None, None)
t1 = TreeNode(3, t2, t3)

s = Solution()
s.levelOrder(t1)

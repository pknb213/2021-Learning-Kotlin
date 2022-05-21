"""
Given the root of a binary tree, return the preorder traversal of its nodes' values.

Example 1:
    Input: root = [1,null,2,3]
    Output: [1,2,3]
Example 2:
    Input: root = []
    Output: []
Example 3:
    Input: root = [1]
    Output: [1]

Constraints:
    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100

Follow up: Recursive solution is trivial, could you do it iteratively?
"""


# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        print(root.val)
        if root.left:
            asd
        elif root.right:
            asd
        else:
            asd
        return [1]


t1 = TreeNode(1, None, 2)
t2 = TreeNode(2, 3, None)
t3 = TreeNode(3, None, None)

s = Solution()
s.preorderTraversal(t1)
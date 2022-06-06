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
from queue import Queue
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        q, res = Queue(), []
        q.put(root)
        while q.qsize():
            footprint, leaf = [], Queue()
            while q.qsize():
                cur = q.get(0)
                print("Current :", cur.val)
                footprint.append(cur.val)
                if cur.left:
                    leaf.put(cur.left)
                if cur.right:
                    leaf.put(cur.right)
                print("Footprint:", footprint, "\nChild:", leaf.qsize(), "Que Size:", q.qsize())
            q = leaf
            res.append(footprint)
            print("Res:", res, "Que:", q.qsize(), "\n")
        print(res)
        return res

        # """ Deque 풀이법 (성능 업) """
        # if root is None:
        #     return root
        # queue = collections.deque()
        # queue.append(root)
        # levels = []
        #
        # while queue:
        #     currentLevel = []
        #     for _ in range(len(queue)):
        #         currentNode = queue.popleft()
        #         currentLevel.append(currentNode.val)
        #         if currentNode.left:
        #             queue.append(currentNode.left)
        #         if currentNode.right:
        #             queue.append(currentNode.right)
        #     levels.append(currentLevel)
        # return levels


t5 = TreeNode(7, None, None)
t4 = TreeNode(15, None, None)
t3 = TreeNode(20, t4, t5)
t2 = TreeNode(9, None, None)
t1 = TreeNode(3, t2, t3)

s = Solution()
s.levelOrder(t1)

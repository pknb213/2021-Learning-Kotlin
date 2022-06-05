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
        """ 오랜만의 기억 속의 DFS 망. 안됨. """
        # if root is None:
        #     return []
        # res = [root.val]
        # while root.right or root.left:
        #     print("Root Value:", root.val)
        #     if root.left:
        #         print("Left :", root.left.val)
        #         res.append(root.left.val)
        #         root = root.left
        #     elif root.right:
        #         print("Right:", root.right.val)
        #         res.append(root.right.val)
        #         root = root.right
        #     else:
        #         print("Empty")
        # print(res)
        # return res

        if root is None: return []
        stack = [root]
        footprint = []

        while stack:
            current_node = stack.pop()
            if current_node:
                footprint.append(current_node.val)
                stack.append(current_node.right)
                stack.append(current_node.left)
        print(footprint)
        return footprint

        """ 아래 코드는 속도가 빠르다. (1) """
        # ans = []
        # stack = [root]
        #
        # while stack:
        #     curr = stack.pop()
        #
        #     if curr:
        #         ans += [curr.val]
        #         stack += [curr.right]
        #         stack += [curr.left]
        #
        # return ans

        """ 아래 코드는 속도가 빠르다. (2) """
        # if root is None:
        #     return []
        #
        # stack, output = [root, ], []
        #
        # while stack:
        #     root = stack.pop()
        #     if root is not None:
        #         output.append(root.val)
        #         if root.right is not None:
        #             stack.append(root.right)
        #         if root.left is not None:
        #             stack.append(root.left)
        #
        # return output

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None: []
        stack = [root]
        footprint = []

        while stack:
            current_node = stack.pop()
            if current_node:
                # print("Current:", current_node.val)
                stack.append(current_node.right)
                stack.append(current_node)
                stack.append(current_node.left)
                # for i in stack:
                #     if i is not None:
                #         print(i.val, end=" ")
                #     else:
                #         print("N", end=" ")
                # print("\n")
            else:
                if stack:
                    current_node = stack.pop()
                    # print("Pop", current_node.val)
                    footprint.append(current_node.val)
        print(footprint)
        return footprint

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None: []
        stack = [root]
        footprint = []
        while stack:
            current_node = stack.pop()
            footprint.append(current_node.val)
            if current_node.left:
                stack.append(current_node.left)
            if current_node.right:
                stack.append(current_node.right)
        print(footprint, footprint[::-1])
        return footprint[::-1]

        """ 좀 더 빠른 성능, visit 사용 """
        # result = []
        # stack = [(root, False)]
        #
        # while stack:
        #     node, visited = stack.pop()
        #     if node:
        #         if visited:
        #             result.append(node.val)
        #         else:
        #             stack.append((node, True))
        #             stack.append((node.right, False))
        #             stack.append((node.left, False))
        # return result


t7 = TreeNode(7, None, None)
t6 = TreeNode(6, None, None)
t5 = TreeNode(5, None, t7)
t4 = TreeNode(4, None, None)
t3 = TreeNode(3, t5, t6)
t2 = TreeNode(2, t4, None)
t1 = TreeNode(1, t2, t3)

# t3 = TreeNode(2, None, None)
# t2 = TreeNode(1, None, None)
# t1 = TreeNode(3, t2, t3)

s = Solution()
s.preorderTraversal(t1)
s.inorderTraversal(t1)
s.postorderTraversal(t1)

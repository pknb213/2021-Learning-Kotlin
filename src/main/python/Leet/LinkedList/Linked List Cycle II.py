"""
Given the head of a linked list, return the node where the cycle begins.
If there is no cycle, return null.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.
Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.
Do not modify the linked list.

Example 1:
    Input: head = [3,2,0,-4], pos = 1
    Output: tail connects to node index 1
    Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
    Input: head = [1,2], pos = 0
    Output: tail connects to node index 0
    Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
    Input: head = [1], pos = -1
    Output: no cycle
    Explanation: There is no cycle in the linked list.

Constraints:
    The number of the nodes in the list is in the range [0, 104].
    -105 <= Node.val <= 105
    pos is -1 or a valid index in the linked-list.

Follow up: Can you solve it using O(1) (i.e. constant) memory?
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # Todo Method 1: Hash Set
        # nodeSet = set()
        # while head:
        #     if head in nodeSet:
        #         print(">>", head.val)
        #         return head
        #     nodeSet.add(head)
        #     head = head.next
        # print(">>", "None")
        # return None

        # Todo Method 2: Floyd's Algorithm
        if head is None or head.next is None:
            return None
        sn, fn = head.next, head.next.next

        while sn != fn:
            print(sn.val, fn.val)
            if fn.next.next is None:
                return None
            sn = sn.next
            fn = fn.next.next

        print("Circle!", sn.val, fn.val)

        sn = head
        while sn != fn:
            print(">>", sn.val, fn.val)
            sn = sn.next
            fn = fn.next
        print(">>", sn.val, fn.val)
        print("Res:", sn.val)
        return sn


n1 = ListNode(3)
n2 = ListNode(2)
n3 = ListNode(0)
n4 = ListNode(-4)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n2
print("Node: 3->2->0->-4 ~> 2")

s = Solution()
s.detectCycle(n1)

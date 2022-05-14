"""
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
    Input: list1 = [1,2,4], list2 = [1,3,4]
    Output: [1,1,2,3,4,4]
Example 2:
    Input: list1 = [], list2 = []
    Output: []
Example 3:
    Input: list1 = [], list2 = [0]
    Output: [0]

Constraints:
    The number of nodes in both lists is in the range [0, 50].
    -100 <= Node.val <= 100
    Both list1 and list2 are sorted in non-decreasing order.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(-1)
        cur = head

        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        # Last Node : next로 null point error 안나게 이동 하지 않게 함
        if l1 is not None:
            cur.next = l1
        else:
            cur.next = l2

        return head.next


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(4)

n1.next = n2
n2.next = n3

n4 = ListNode(1)
n5 = ListNode(3)
n6 = ListNode(4)

n4.next = n5
n5.next = n6

l1 = [n1, n2, n3]
l2 = [n4, n5, n6]


print("L1: 1->2->4, L2: 1->3->4")
s = Solution()
# 문제가 이해가 안가, 씨발 l1, l2의 next 노드를 순차적으로 준다는 건가 씨발
s.mergeTwoLists(l1, l2)
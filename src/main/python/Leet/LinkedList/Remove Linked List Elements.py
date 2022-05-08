"""
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val,
and return the new head.

Example 1:
    Input: head = [1,2,6,3,4,5,6], val = 6
    Output: [1,2,3,4,5]

Example 2:
    Input: head = [], val = 1
    Output: []

Example 3:
    Input: head = [7,7,7,7], val = 7
    Output: []

Constraints:
    The number of nodes in the list is in the range [0, 104].
    1 <= Node.val <= 50
    0 <= val <= 50
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # Todo: 콘솔은 되는디
        # if head is None or head.next is None:
        #     return None
        #
        # while head:
        #     prev, next = head, head.next
        #     print(prev.val, next.val)
        #     if next.val == val:
        #         print("!!! Delete Next Node")
        #         if next.next is None:
        #             head.next = None
        #         else:
        #             print(head.next.val)
        #             head.next = next.next
        #     head = head.next
        #
        # return head
        # # Todo: Dummy 생성 방법
        # dummyHead = ListNode(None)
        # dummyHead.next = head
        # node = dummyHead
        #
        # while node.next:
        #     if node.next.val == val:
        #         node.next = node.next.next
        #     else:
        #         node = node.next
        #
        # return dummyHead.next

        # Todo: 빠른 테스트
        while head and head.val == val:
            head = head.next
        if not head:
            return head
        next_node = head
        while next_node and next_node.next:
            if next_node.next.val == val:
                next_node.next = next_node.next.next
            else:
                next_node = next_node.next

        return head


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(6)
n4 = ListNode(3)
n5 = ListNode(4)
n6 = ListNode(5)
n7 = ListNode(6)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7

n = 6
print("Node: 1->2->6->3->4->5->6", "n:", n)
s = Solution()
s.removeElements(n1, n)
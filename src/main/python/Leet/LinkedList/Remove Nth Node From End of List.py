"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
    Input: head = [1,2,3,4,5], n = 2
    Output: [1,2,3,5]

Example 2:
    Input: head = [1], n = 1
    Output: []

Example 3:
    Input: head = [1,2], n = 1
    Output: [1]

Constraints:
    The number of nodes in the list is sz.
    1 <= sz <= 30
    0 <= Node.val <= 100
    1 <= n <= sz

Follow up: Could you do this in one pass?
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Todo: 포인터 두 개를 만든 후, n 만큼 거리를 벌리고 null까지 이동하면 뒤에서 n번 만큼 떨어진 노드를 알 수 있다.

        tmp = ListNode()
        tmp.next = head

        p1, p2 = head, head

        for i in range(n):
            print(p1.val, i)
            if p1.next is None:
                return head.next
            p1 = p1.next
        print(">", p1.val)

        while p1.next:
            print(p1.val, p2.val)
            p1 = p1.next
            p2 = p2.next
        print(">>", p1.val, p2.val)
        p2.next = p2.next.next

        return head

        # Todo : 좀 더 빠르게 하는 방법이며, Dummy Linkedlist를 생성해서 테스트 케이스까지 고려하는 방법이다.
        dummy = ListNode(-1)
        dummy.next = head
        slow = dummy
        fast = head
        while n > 0 and fast:
            fast = fast.next
            n -= 1
        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next

n1 = ListNode(1)
n2 = ListNode(2)

n1.next = n2

n = 2

print("Node1: 1->2", "  Del Back Index:", n)

s = Solution()
s.removeNthFromEnd(n1, n)
"""
Given the head of a singly linked list, group all the nodes with odd indices together followed
by the nodes with even indices, and return the reordered list.
The first node is considered odd, and the second node is even, and so on.
Note that the relative order inside both the even and odd groups should remain as it was in the input.
You must solve the problem in O(1) extra space complexity and O(n) time complexity.

Example 1:
    Input: head = [1,2,3,4,5]
    Output: [1,3,5,2,4]

Example 2:
    Input: head = [2,1,3,5,6,4,7]
    Output: [2,3,6,7,1,5,4]

Constraints:
    The number of nodes in the linked list is in the range [0, 104].
    -106 <= Node.val <= 106
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        """
        Todo: 원래 의도: odd, even을 구별하여 연결리스트 만들고 나중에 붙이기.
        실패 이유: even의 스타트 지점을 생각 못함
        """
        # if head is None or head.next is None:
        #     return None
        #
        # if head.next.next:
        #     odd, even = head, head.next
        #     head = head.next.next
        # else:
        #     return head
        #
        # raw = odd
        # seven = even
        #
        # while head:
        #     if head.next is None or head.next.next is None:
        #         break
        #     else:
        #         print(head.val, head.next.val)
        #         odd.next, even.next = head, head.next
        #         print(odd.val, odd.next.val, even.val, even.next.val)
        #     print(head.next.next.val)
        #     head = head.next.next
        #     print(head.val)
        #
        # odd.next = seven
        #
        # while raw:
        #     print(raw.val, end="->")
        #     raw = raw.next
        #
        # return head

        # Todo: 풀이
        start_point = head
        if head is None or head.next is None:
            return None

        odd = head
        even = head.next
        even_head = head.next

        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next

        odd.next = even_head

        while start_point:
            print(start_point.val, end="->")
            start_point = start_point.next

        return head

        # Todo: 이게 위 풀이보다 훨 빠름
        if not head or not head.next:
            return head

        odd = head
        even = head.next
        evenHead = even

        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd, even = odd.next, even.next

        odd.next = evenHead
        return head


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

print("Node: 1->2->3->4->5")
s = Solution()
s.oddEvenList(n1)
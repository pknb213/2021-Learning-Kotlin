"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
    Input: head = [1,2,3,4,5]
    Output: [5,4,3,2,1]

Example 2:
    Input: head = [1,2]
    Output: [2,1]

Example 3:
    Input: head = []
    Output: []

Constraints:
    The number of nodes in the list is the range [0, 5000].
    -5000 <= Node.val <= 5000

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # Todo: 재귀 함수
        # def reverse(node: ListNode, prev: ListNode = None ):
        #     # base case
        #     if not node:
        #         return prev
        #
        #     # recursive case
        #     # next 변수에 현재 노드의 next를 넣고 매개변수 node로 재귀 호출, node.next에는 이전 호출의 노드를 재할당
        #     next, node.next = node.next, prev
        #     # next가 재귀 호출 시 매개변수 node 자리로 들어감, 현재 node는 prev 자리로 들어감
        #     return reverse(next, node)
        # return reverse(head)

        # Todo: 반복
        node, prev = head, None

        while node:
            print(node.val)
            # node.next를 이전 prev 리스트로 계속 연결하면서 끝날 때까지 반복
            next, node.next = node.next, prev
            prev, node = node, next
        return prev

        # Todo: 출력 확인
        # while dumy:
        #     print(dumy.val, end="")
        #     if dumy.next is None:
        #         break
        #     else:
        #         print("->", end="")
        #     dumy = dumy.next


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

print("Node: 1->2->3")

s = Solution()
s.reverseList(n1)
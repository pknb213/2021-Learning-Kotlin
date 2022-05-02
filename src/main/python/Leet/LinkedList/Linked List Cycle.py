"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.
Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
    Input: head = [3,2,0,-4], pos = 1
    Output: true
    Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
    Input: head = [1,2], pos = 0
    Output: true
    Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
    Input: head = [1], pos = -1
    Output: false
    Explanation: There is no cycle in the linked list.

Constraints:
    The number of the nodes in the list is in the range [0, 104].
    -105 <= Node.val <= 105
    pos is -1 or a valid index in the linked-list.

참고
    해당 문제는 연결리스트가 순회하는지 체크하는 기본 문제이다.
    Input으로 주어지는 연결리스트의 객체 정보는 위에 주석처리 되어 있으므로 참고해서 알고리즘을 짜면 된다.

"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        print(head, head.val, head.next)
        if head is None or head.next is None:
            return False

        slowNode = head
        fastNode = head.next

        print(">", slowNode.val, fastNode.val)

        while fastNode != slowNode:
            if fastNode is None or fastNode.next is None:
                return False
            else:
                fastNode = fastNode.next.next
                slowNode = slowNode.next
                print(">>", slowNode.val, fastNode.val, "\n")

        return True


ll = ListNode([3,2,0,-4])
s = Solution()
s.hasCycle(ll)


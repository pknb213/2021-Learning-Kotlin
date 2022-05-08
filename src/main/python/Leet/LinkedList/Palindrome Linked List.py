"""
Given the head of a singly linked list, return true if it is a palindrome.

Example 1:
    Input: head = [1,2,2,1]
    Output: true

Example 2:
    Input: head = [1,2]
    Output: false

Constraints:
    The number of nodes in the list is in the range [1, 105].
    0 <= Node.val <= 9

Follow up: Could you do it in O(n) time and O(1) space?
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # Temp pointer
        slow = head

        # Declare a stack
        stack = []

        ispalin = True

        # Push all elements of the list
        # to the stack
        while slow != None:
            stack.append(slow.val)

            # Move ahead
            slow = slow.next

        # Iterate in the list again and
        # check by popping from the stack
        while head != None:

            # Get the top most element
            i = stack.pop()

            # Check if data is not
            # same as popped element
            if head.val == i:
                ispalin = True
            else:
                ispalin = False
                break

            # Move ahead
            head = head.next

        return ispalin


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
s.isPalindrome(n1)
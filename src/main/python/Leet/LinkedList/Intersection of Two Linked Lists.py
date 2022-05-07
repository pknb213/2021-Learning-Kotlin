"""
Given the heads of two singly linked-lists headA and headB,
return the node at which the two lists intersect.
If the two linked lists have no intersection at all, return null.
For example, the following two linked lists begin to intersect at node c1:

The test cases are generated such that there are no cycles anywhere in the entire linked structure.
Note that the linked lists must retain their original structure after the function returns.
Custom Judge:

The inputs to the judge are given as follows (your program is not given these inputs):

- intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
- listA - The first linked list.
- listB - The second linked list.
- skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
- skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.

The judge will then create the linked structure based on these inputs and pass the two heads, headA and headB to your program.
If you correctly return the intersected node, then your solution will be accepted.

Example 1:
    Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
    Output: Intersected at '8'
    Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
    From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5].
    There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.

Example 2:
    Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
    Output: Intersected at '2'
    Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect).
    From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4].
    There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.

Example 3:
    Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
    Output: No intersection
    Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5].
    Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
    Explanation: The two lists do not intersect, so return null.

Constraints:
    The number of nodes of listA is in the m.
    The number of nodes of listB is in the n.
    1 <= m, n <= 3 * 104
    1 <= Node.val <= 105
    0 <= skipA < m
    0 <= skipB < n
    intersectVal is 0 if listA and listB do not intersect.
    intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.

Follow up: Could you write a solution that runs in O(m + n) time and use only O(1) memory?
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        head A, B를 따라가면서 교차 지점이 있는지 조건을 주어야한다
        교차지점이 없으면 intersectVal = 0을 준다.
        떠오른 Hashset 방법 : 지나간 노드를 각각의 Set에 저장한다. 그리고 교집합을 이용하여 교차 지점을 구한다.

        아래 형태로 접근하면 Runtime이 너무 길어진다.
        """
        # if headA is None or headB is None:
        #     return None
        #
        # a_set = set()
        # b_set = set()
        #
        # while headA and headB:
        #     print(headA.val, headB.val)
        #     if headA is not None:
        #         a_set.add(headA.val)
        #     if headB is not None:
        #         b_set.add(headB.val)
        #     if a_set.intersection(b_set):
        #         break
        #     elif headA.next is None and headB.next is None:
        #         return None
        #     if headA.next:
        #         headA = headA.next
        #     if headB.next:
        #         headB = headB.next
        #
        # print(a_set, b_set)
        # print(a_set.intersection(b_set))
        #
        # if a_set.intersection(b_set):
        #     return a_set.intersection(b_set).pop()
        # return None

        a_map = set() #hashMap(hashSet)사용

        while headA: #순회하며 set에 각 노드를 넣고
            a_map.add(headA)
            headA = headA.next

        while headB:
            if headB in a_map: #head(로 시작하는 연결리스트가)가 set에 있는지 확인
                return headB
            else:
                headB = headB.next
        return None

        res=set()

        # Todo: 의문 위와 아래의 코드는 거의 일치하는데 아래가 더 많이 빠르다.

        while headA:
            res.add(headA)
            headA=headA.next
        while headB:
            if headB not in res:
                res.add(headB)
            else:
                return headB
            headB=headB.next
        return None

n1 = ListNode(1)
n2 = ListNode(9)
n3 = ListNode(1)
# n4 = ListNode(2) # 교차 O
# n5 = ListNode(4)
n4 = ListNode(6) # 교차 X
n5 = ListNode(9)

nn1 = ListNode(3)
nn2 = ListNode(2)
nn3 = ListNode(4)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

nn1.next = nn2
nn2.next = nn3

print("Node1: 1->9->1->2->4\nNode2: 3->2->4")

s = Solution()
s.getIntersectionNode(n1, nn1)

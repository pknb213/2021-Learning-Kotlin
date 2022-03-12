"""
https://leetcode.com/explore/learn/card/fun-with-arrays/525/inserting-items-into-an-array/3245/
LeetCode : Duplicate Zeros

Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.
Do the above modifications to the input array in place and do not return anything.

Example 1:
    Input: arr = [1,0,2,3,0,4,5,0]
    Output: [1,0,0,2,3,0,0,4]
    Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

Example 2:
    Input: arr = [1,2,3]
    Output: [1,2,3]
    Explanation: After calling your function, the input array is modified to: [1,2,3]

Constraints:
    1 <= arr.length <= 104
    0 <= arr[i] <=

    @ 주의 할점
    deque써서 할 때, 배열 2개를 사용해서 메모리 성능이 나빠지며,
    아래 써있다 싶이 return으로 배열을 반환하는 것이 아니라
    주어진 arr의 순서를 변경해야 한다.

    그렇기 때문에 새로운 배열을 쓰는 것을 추천하지 않는다.
    아래 코드는 성능 최적화가 되지 않았다. 배열 생성과 if 절의 구문을 최적화하면 더 빨라질 것이다.
"""
from typing import List
from collections import deque


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        # print(arr)
        size = len(arr)
        idx = 0
        while idx < size:
            print(idx, "<=", size)
            print(arr[idx], arr)
            if arr[idx] == 0:
                arr.pop()
                arr.insert(idx, 0)
                idx += 2
            else:
                idx += 1
        print(arr)

        """
        deq = deque(arr)
        for i, v in enumerate(arr):
            if v == 0:
                deq.pop()
                deq.insert(i, 0)
        arr = deq
        """


input_arr = [1,0,2,3,0,4,5,0]
s = Solution()
s.duplicateZeros(input_arr)

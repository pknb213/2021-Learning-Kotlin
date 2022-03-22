"""
Given an array arr, replace every element in that array with the greatest element among the elements to its right,
and replace the last element with -1.

After doing so, return the array.

Example 1:
    Input: arr = [17,18,5,4,6,1]
    Output: [18,6,6,6,1,-1]
Explanation:
    - index 0 --> the greatest element to the right of index 0 is index 1 (18).
    - index 1 --> the greatest element to the right of index 1 is index 4 (6).
    - index 2 --> the greatest element to the right of index 2 is index 4 (6).
    - index 3 --> the greatest element to the right of index 3 is index 4 (6).
    - index 4 --> the greatest element to the right of index 4 is index 5 (1).
    - index 5 --> there are no elements to the right of index 5, so we put -1.
Example 2:
    Input: arr = [400]
    Output: [-1]
    Explanation: There are no elements to the right of index 0.

Constraints:
    1 <= arr.length <= 104
    1 <= arr[i] <= 105

    @ 주의 사항
    아래 솔류션으로 하면 상당히 실행 시간면에서 좋지 않은 효율을 보여 준다.
    빠른 실행시간 지닌 코드의 예제도 같이 아래에 있다.
"""
from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # p = 0
        # while p != len(arr)-1:
        #     print("탐색:", p, "해당: ", arr[p], "max:", max(arr[p+1:]), arr)
        #     arr[p] = max(arr[p+1:])
        #     p += 1
        # arr[-1] = -1
        # print(arr)
        # return arr
        mx = -1
        for i in range(len(arr) - 1, -1, -1):  # 5, 4, 3, 2, 1, 0
            print(">>", i, len(arr)-1, arr, arr[i])
            print(arr[i], mx, max(mx, arr[i]), arr)
            arr[i], mx = mx, max(mx, arr[i])
            # arr[i] = mx
            # mx = max(mx, arr[i])
            """
            arr[i] = mx
            mx = max(mx, arr[i])
            """
            print(arr[i], mx, max(mx, arr[i]), arr)
            # arr[i], mx = mx, max(mx, arr[i])
        print(arr)
        return arr


nums = [17,18,5,4,6,1]
s = Solution()
s.replaceElements(nums)

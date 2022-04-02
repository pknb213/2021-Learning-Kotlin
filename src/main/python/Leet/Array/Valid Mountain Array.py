"""
https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3251/
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Example 1:
    Input: arr = [2,1]
    Output: false

Example 2:
    Input: arr = [3,5,5]
    Output: false

Example 3:
    Input: arr = [0,3,2,1]
    Output: true

Constraints:
    1 <= arr.length <= 104
    0 <= arr[i] <= 104
"""
from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        p = 0

        # index가 증가함에 따라 값도 커야 한다. (오르막)
        while p+1 < n and arr[p] < arr[p+1]:
            p += 1

        # 정상은 시작 index, 마지막 index이면 안된다.
        if p == 0 or p == n - 1:
            return False

        # index가 증가함에 따라 값도 작아져야 한다. (내리막)
        while p+1 < n and arr[p] > arr[p+1]:
            p += 1

        print(p, n-1)
        return p == n-1

nums = [3,5,5,4,3,2,1]
s = Solution()
s.validMountainArray(nums)

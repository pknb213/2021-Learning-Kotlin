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
        if len(arr) < 3:
            print("False")
            return False
        print(arr)
        top = max(arr)
        top_idx = arr.index(top)
        print("Top:", top, "idx:", top_idx)

        incre = arr[:top_idx+1]
        decre = arr[top_idx:]
        print(incre, decre)

        

        return False


nums = [3,5,5,4,3,2,1]
s = Solution()
s.validMountainArray(nums)

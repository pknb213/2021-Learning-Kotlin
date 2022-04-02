"""
Given an integer array nums sorted in non-decreasing order,
return an array of the squares of each number sorted in non-decreasing order.

Example 1:
    Input: nums = [-4,-1,0,3,10]
    Output: [0,1,9,16,100]
    Explanation: After squaring, the array becomes [16,1,0,9,100].
    After sorting, it becomes [0,1,9,16,100].

Example 2:
    Input: nums = [-7,-3,2,3,11]
    Output: [4,9,9,49,121]

Constraints:
    1 <= nums.length <= 104
    -104 <= nums[i] <= 104
    nums is sorted in non-decreasing order.

Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
"""
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Todo: sorted() 메서드 사용 -> 새로운 객체를 생성
        # return sorted([i**2 for i in nums])

        # Todo: sort() 메서드 사용 -> 객체 자체를 변경
        sol = [x*x for x in nums]
        sol.sort()
        return sol


arr = [-4,-1,0,3,10]
s = Solution()
s.sortedSquares(arr)
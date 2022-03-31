"""
Given an array nums of n integers where nums[i] is in the range [1, n],
return an array of all the integers in the range [1, n] that do not appear in nums.

Example 1:
    Input: nums = [4,3,2,7,8,2,3,1]
    Output: [5,6]

Example 2:
    Input: nums = [1,1]
    Output: [2]

Constraints:
    n == nums.length
    1 <= n <= 105
    1 <= nums[i] <= n

Follow up: Could you do it without extra space and in O(n) runtime?
You may assume the returned list does not count as extra space.
"""
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        le = len(nums)
        if le > max(nums):
            return [le]
        nums = sorted(list(set(nums)), reverse=True)
        print(nums)
        p = nums.pop()
        if p != 1:
            res += [i for i in range(1, p)]
        while len(nums):
            p2 = nums.pop()
            print(p, p2)
            if p+1 != p2:
                res.append(p+1)
            p = p+1
        print(res)
        return res


arr = [2,2,5]
s = Solution()
s.findDisappearedNumbers(arr)
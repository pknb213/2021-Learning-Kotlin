"""
Given an array of integers nums which is sorted in ascending order, and an integer target,
write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
    Input: nums = [-1,0,3,5,9,12], target = 9
    Output: 4
    Explanation: 9 exists in nums and its index is 4

Example 2:
    Input: nums = [-1,0,3,5,9,12], target = 2
    Output: -1
    Explanation: 2 does not exist in nums so return -1

Constraints:
    1 <= nums.length <= 104
    -104 < nums[i], target < 104
    All the integers in nums are unique.
    nums is sorted in ascending order.
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        le = len(nums)
        inx = 0
        print(le,  le//2, nums[le//2], nums)
        while nums:
            mid = len(nums) // 2
            print(inx, nums, mid)
            if nums[mid] == tar:
                print(inx+mid, "!!!")
                return inx + mid
            else:
                if len(nums) <= 1:
                    print("-1, Fail")
                    return -1
                elif tar > nums[mid]:
                    inx += mid
                    nums = nums[mid:]
                else:
                    nums = nums[:mid]
        return -1

        # Todo: 속도가 이게 더 빠름: nums 배열을 잘라서 다시 할당하지 않고 left, right index를 통해 계산
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1


li = [-1,0,3,5,9,12]
tar = 9

s = Solution()
s.search(li, tar)




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

@주의 할점
아래 처럼 List Comprehension 사용하는 것이 파이썬에서 알고리즘 풀 때 가장 먼저 떠오르는 방법이다.
하지만 아래 처럼 return에 컴프레션으로 풀게되면 타임오버가 걸린다.
해당 문제는 그 보다 더 빠른 차집합(Difference set)을 이용 한다.
"""
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # set_arr = list(set(nums))
        # print([i for i in range(1, len(nums)+1)])
        # print([x for x in [i for i in range(1, len(nums)+1)] if x not in set_arr])
        # return [x for x in [i for i in range(1, len(nums)+1)] if x not in set_arr]

        return list(set(range(1, len(nums) + 1)) - set(nums))

arr = [1,1,2,2]
s = Solution()
s.findDisappearedNumbers(arr)
"""
Given an integer array nums, return the third distinct maximum number in this array.
If the third maximum does not exist, return the maximum number.

Example 1:
    Input: nums = [3,2,1]
    Output: 1
    Explanation:
    The first distinct maximum is 3.
    The second distinct maximum is 2.
    The third distinct maximum is 1.

Example 2:
    Input: nums = [1,2]
    Output: 2
    Explanation:
    The first distinct maximum is 2.
    The second distinct maximum is 1.
    The third distinct maximum does not exist, so the maximum (2) is returned instead.

Example 3:
    Input: nums = [2,2,3,1]
    Output: 1
    Explanation:
    The first distinct maximum is 3.
    The second distinct maximum is 2 (both 2's are counted together since they have the same value).
    The third distinct maximum is 1.

Constraints:
    1 <= nums.length <= 104
    -231 <= nums[i] <= 231 - 1

Follow up: Can you find an O(n) solution?

@ 주의 사항
Runtime: 93 ms
Memory Usage: 15.5 MB
상위 27.40% 에 해당 하는 time complexity가 나온다.

"""
from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        if len(nums) < 3:
            return max(nums)
        for i in range(3):
            if i == 2:
                return max(nums)
            nums.remove(max(nums))

        # Todo: 아래 코드는 중복을 set casting으로 없애고, 정렬을 하여 문제에서 제기한 3번째 인수의 값을
        # Todo: 출력하는 코드와 3개 이하일 때의 조건을 삼항 연산자로 return한 모습이다.
        # nums = list(set(nums))
        # nums.sort()
        # return nums[-3] if len(nums) >= 3 else nums[-1]

        # Todo: 아래는 마지막 조건 및 출력을 삼항 연산자를 이용하지 않는 방법인데, 속도 차이가 15% 정도 난다.
        # s = set(nums)
        # l = list(s)
        # l.sort()
        # if len(l) == 1 or len(l) == 2:
        #     return l[-1]
        # return l[-3]

arr = [2,2,3,1]
s = Solution()
s.thirdMax(arr)

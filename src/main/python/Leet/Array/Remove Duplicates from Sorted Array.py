"""
https://leetcode.com/explore/learn/card/fun-with-arrays/526/deleting-items-from-an-array/3248/
Given an integer array nums sorted in non-decreasing order,
remove the duplicates in-place such that each unique element appears only once.
The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages,
you must instead have the result be placed in the first part of the array nums. More formally,
if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result.
It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.
Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Custom Judge:
The judge will test your solution with the following code:

    int[] nums = [...]; // Input array
    int[] expectedNums = [...]; // The expected answer with correct length

    int k = removeDuplicates(nums); // Calls your implementation

    assert k == expectedNums.length;
    for (int i = 0; i < k; i++) {
        assert nums[i] == expectedNums[i];
    }

If all assertions pass, then your solution will be accepted.


Example 1:
    Input: nums = [1,1,2]
    Output: 2, nums = [1,2,_]
    Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
    It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:
    Input: nums = [0,0,1,1,1,2,2,3,3,4]
    Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
    Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
    It does not matter what you leave beyond the returned k (hence they are underscores).

Constraints:
    1 <= nums.length <= 3 * 104
    -100 <= nums[i] <= 100
    nums is sorted in non-decreasing order.

    @ 주의할점
    아래 코드처럼 하면 실행시간 효율이 매우 나쁘다. 평균 150ms인데 590ms이 걸렸기 때문이다.
    주석 코드로 실행하면 88ms 정도 걸리고, 그 이유는 이중 포문을 사용하지 않은 것이 크다.

"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        print(nums)
        p = 0
        ct = 0
        for i, v in enumerate(nums):
            print("before", p, i, nums)
            if p == i:
                print("Next")
                ct += 1
                continue
            elif nums[p] < v:
                print(">> Next !!!", nums[p], v)
                p += 1
                ct += 1
            else:
                for j in range(i+1, len(nums)):
                    print("Circulation", i, j, nums)
                    if nums[p] < nums[j]:
                        print("> Break", nums[i], nums[j])
                        nums[i] = nums[j]
                        ct += 1
                        p += 1
                        break
                    elif j == len(nums) - 1:
                        print(ct, nums)
                        return ct

            print("after", p, i, v, nums)

        print(ct, nums)
        return ct

        # l = 1
        #
        # for r in range(1, len(nums)):
        #     if nums[r] != nums[r-1]:
        #         nums[l] = nums[r]
        #         l += 1
        #
        # return l


nums = [0,0,1,1,1,2,2,3,3,4]
s = Solution()
s.removeDuplicates(nums)

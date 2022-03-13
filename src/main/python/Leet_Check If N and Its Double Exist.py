"""
Given an array arr of integers,
check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).

More formally check if there exists two indices i and j such that :

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]

Example 1:
    Input: arr = [10,2,5,3]
    Output: true
    Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.

Example 2:
    Input: arr = [7,1,14,11]
    Output: true
    Explanation: N = 14 is the double of M = 7,that is, 14 = 2 * 7.

Example 3:
    Input: arr = [3,1,7,11]
    Output: false
    Explanation: In this case does not exist N and M, such that N = 2 * M.

Constraints:
    2 <= arr.length <= 500
    -10^3 <= arr[i] <= 10^3

    @ 주의 할점
    성능 개선을 위해서는 Hash, Set 등 자료구조를 이용해야한다.
    해당 문제는 binary search에 속하지만 정작 성능은 자료구조를 이용하는 편이 빠르다.
"""
from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        for idx, i in enumerate(arr):
            if i % 2 == 0:
                target = i/2
                # print("Search:", i, "target:", target, arr)
                str = 0
                ed = len(arr) - 1
                while str <= ed:
                    mid = (str + ed) // 2
                    # print("\tidx", str, "~", ed, "Mid:", mid, "=>", arr[mid])
                    if arr[mid] == target and idx != mid:
                        # print(target, "!!")
                        return True
                    elif arr[mid] < target:
                        # print("\t", arr[mid], "<", target, "str=>", mid+1)
                        str = mid + 1
                    else:
                        # print("\t", arr[mid], ">=", target, "ed=>", mid-1)
                        ed = mid - 1
        # print("False")
        return False

        # for i in range(0,len(arr)):
        #     if arr[i] == 0:
        #         print(len([x for x in arr if x == 0]))
        #         if len([x for x in arr if x == 0]) > 1:
        #             return True
        #     elif arr[i]*2 in arr:
        #         return True
        #
        # return False

nums = [-2,0,10,-19,4,6,-8]
s = Solution()
s.checkIfExist(nums)

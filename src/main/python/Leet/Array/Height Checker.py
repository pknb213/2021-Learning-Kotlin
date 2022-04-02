"""
A school is trying to take an annual photo of all the students.
The students are asked to stand in a single file line in non-decreasing order by height.
Let this ordering be represented by the integer array expected where
expected[i] is the expected height of the ith student in line.
You are given an integer array heights representing the current order that
the students are standing in.
Each heights[i] is the height of the ith student in line (0-indexed).

Return the number of indices where heights[i] != expected[i].

Example 1:
    Input: heights = [1,1,4,2,1,3]
    Output: 3
    Explanation:
    heights:  [1,1,4,2,1,3]
    expected: [1,1,1,2,3,4]
    Indices 2, 4, and 5 do not match.

Example 2:
    Input: heights = [5,1,2,3,4]
    Output: 5
    Explanation:
    heights:  [5,1,2,3,4]
    expected: [1,2,3,4,5]
    All indices do not match.

Example 3:
    Input: heights = [1,2,3,4,5]
    Output: 0
    Explanation:
    heights:  [1,2,3,4,5]
    expected: [1,2,3,4,5]
    All indices match.

Constraints:
    1 <= heights.length <= 100
    1 <= heights[i] <= 100

@ 주의사항
    Runtime: 70 ms
    Memory Usage: 13.8 MB
    sorted한 배열을 생성 후에 range로 각 요소를 비교해서 count를 올리는 방식으로는
    상위 70%에 해당 하는 느린 time complexity가 굉장히 느리다.


"""
from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        cnt = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                cnt += 1
        return cnt

        # Todo: 아래의 경우, 정렬된 배열을 만든 후 zip을 이용하여 각 요소를 비교하여 바로 sum으로 집계한다. 해당 상위 28% 속도를 보여준다.
        # expected = sorted(heights)
        # return sum(ah != eh for ah, eh in zip(heights, expected))

        # Todo: 아래의 경우, sort() 메서드를 이용해 새 객체를 생성하지 않기 때문에 time complexity가 높게 된다.
        # expected = heights[:]
        # expected.sort()
        # res = 0
        # for i in range (0,len(heights)):
        #     if heights[i]!=expected[i]:
        #         res += 1
        # return res


arr = [5,1,2,3,4]
s = Solution()
s.heightChecker(arr)

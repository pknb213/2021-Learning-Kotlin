"""
There are n cities. Some of them are connected, while some are not.
If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.
A province is a group of directly or indirectly connected cities and no other cities outside of the group.
You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.
Return the total number of provinces.

Example 1:
    Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
    Output: 2

Example 2:
    Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
    Output: 3

Constraints:
    1 <= n <= 200
    n == isConnected.length
    n == isConnected[i].length
    isConnected[i][j] is 1 or 0.
    isConnected[i][i] == 1
    isConnected[i][j] == isConnected[j][i]

주의할점
그래프 순회 문제로 DFS, BPS 앞고리즘을 고려해야한다.

"""
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        for i in isConnected:
            print(i)
        n = len(isConnected)
        visit = set()

        def dfs(c1, c2):
            if (c1, c2) in visit or (c2, c1) in visit:
                return
            visit.add((c1, c2))
            visit.add((c2, c1))
            for cn in range(n):
                if isConnected[c1][cn] and (c1, cn) not in visit:
                    dfs(c1, cn)
                if isConnected[c2][cn] and (c2, cn) not in visit:
                    dfs(c2, cn)

        cnt = 0
        for c1 in range(n):
            for c2 in range(n):
                if isConnected[c1][c2] and (c1, c2) not in visit:
                    cnt += 1
                    dfs(c1, c2)
        print(cnt)
        return cnt


arr = [[1,1,0],[1,1,0],[0,0,1]]
s = Solution()
s.findCircleNum(arr)


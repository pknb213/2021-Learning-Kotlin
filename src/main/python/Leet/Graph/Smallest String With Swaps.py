"""
You are given a string s, and an array of pairs of indices in
the string pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.
You can swap the characters at any pair of indices in the given pairs any number of times.
Return the lexicographically smallest string that s can be changed to after using the swaps.

Example 1:
    Input: s = "dcab", pairs = [[0,3],[1,2]]
    Output: "bacd"
Explaination:
    Swap s[0] and s[3], s = "bcad"
    Swap s[1] and s[2], s = "bacd"

Example 2:
    Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
    Output: "abcd"
Explaination:
    Swap s[0] and s[3], s = "bcad"
    Swap s[0] and s[2], s = "acbd"
    Swap s[1] and s[2], s = "abcd"

Example 3:
    Input: s = "cba", pairs = [[0,1],[1,2]]
    Output: "abc"
Explaination:
    Swap s[0] and s[1], s = "bca"
    Swap s[1] and s[2], s = "bac"
    Swap s[0] and s[1], s = "abc"

Constraints:
    1 <= s.length <= 10^5
    0 <= pairs.length <= 10^5
    0 <= pairs[i][0], pairs[i][1] < s.length
    s only contains lower case English letters.

주의 사항
문제를 잘 읽자. 해당 문제는 서로소 집합 문제이다. (Disjoint Set)
그 아래는 DFS, Union Find 방법으로 푼 예시를 보여준다.
"""
from typing import List


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        # 생각 없는 구더기 풀이 방법
        # text = list(s)
        # for x, y in pairs:
        #     tmp = text[y:y+1]
        #     text[y:y+1] = text[x:x+1]
        #     text[x:x+1] = tmp
        # return "a"

        """ DFS 방법 """
        """
            st = "dcab"
            arr = [[0,3],[1,2],[0,2]]
        """
        # from collections import defaultdict
        # d = defaultdict(list)  # 인접 리스트 저장용 해시맵 Dict<List<Char>>
        # s = list(s)  # 문자열 to 리스트
        # visited = [False for _ in range(len(s))]  # 방문의 경우 Boolean 타입으로 충분, 또는 0, 1
        #
        # for source, destination in pairs:  # 인접 리스트(adj list) 만들기
        #     d[source].append(destination)
        #     d[destination].append(source)
        # print("String:", s, "\nAdjacency list: ", d)
        #
        # def dfs(search_list, index, chars, indices):  # dfs 구현
        #     if visited[index]:  # 이미 방문 함 -> 패스
        #         print("이미 방문", visited)
        #         return
        #     print("방문 리스트", visited, "\n방문할 곳:", index)
        #     chars.append(search_list[index])  # 문자열 저장
        #     indices.append(index)  # 주소 저장
        #     visited[index] = True   # 방문 기록
        #     print("문자 리스트:", chars, "주소 리스트", indices)
        #     for neigh in d[index]:  # 인접 노드 dfs 수행
        #         print("<인접 노드", neigh, ">", end=" ")
        #         dfs(search_list, neigh, chars, indices)
        #
        # for i in range(len(s)):  # 주어진 문자열 모두 vertex(정점)으로 시작
        #     if not visited[i]:  # 해당 정점이 아직 방문하지 않으면 dfs 수행
        #         chars = []  # 문자 리스트
        #         indices = []  # 주소 리스트
        #         print(i,"Vertex DFS 수행")
        #         dfs(s, i, chars, indices)  # DFS 함수 시작
        #         chars = sorted(chars)  # 정렬
        #         indices = sorted(indices)  # 정렬
        #         print("\n정렬된 문자 리스트:", chars, "\n정렬된 주소 리스트:", indices)
        #         for c, i in zip(chars, indices):  # 두 리스트의 각 요소를 하나로 합쳐서 반복
        #             s[i] = c
        #         print(">> String:", s, "\n")
        #     else:
        #         print(i, "Vertex DFS 이미 수행.")
        # return "".join(s)

        """ Union Find 방법 """
        from collections import defaultdict
        s = list(s)  # String to List
        nodes = [i for i in range(len(s))]  # Node 리스트 생성
        size = [1 for i in range(len(s))]

        def find(x):  # 찾기 메서드
            if x == nodes[x]:
                return x
            nodes[x] = find(nodes[x])
            return nodes[x]

        def union(x, y):  # 결합 메서드
            rootx = find(x)
            rooty = find(y)
            if rootx != rooty:
                nodes[rooty] = rootx

        for e1, e2 in pairs:
            union(e1, e2)

        rootToComponent = defaultdict(list)

        for i in range(len(s)):
            root = find(i)
            rootToComponent[root].append(i)

        for k, indices in rootToComponent.items():
            chars = []
            for i in indices:
                chars.append(s[i])
            chars = sorted(chars)

            for c, i in zip(chars, indices):
                s[i] = c

        print(s)
        return "".join(s)


st = "dcab"
arr = [[0,3],[1,2]]
s = Solution()
s.smallestStringWithSwaps(st, arr)

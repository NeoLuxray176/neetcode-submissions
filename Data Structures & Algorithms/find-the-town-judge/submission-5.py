class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegree = [0] * (n + 1)
        outdegree = [0] * (n + 1)

        for a, b in trust:
            outdegree[a] += 1
            indegree[b] += 1

        for i in range(n + 1):
            if outdegree[i] == 0 and indegree[i] == n - 1:
                return i

        return -1
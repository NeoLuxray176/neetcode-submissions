class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = [0] * numCourses
        adj_list = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            indegrees[a] += 1
            adj_list[b].append(a)

        queue = [i for i, x in enumerate(indegrees) if x == 0]

        res = []

        while queue:
            curr = queue.pop()

            res.append(curr)

            for u in adj_list[curr]:
                indegrees[u] -= 1
                if indegrees[u] == 0:
                    queue.append(u)

        if len(res) == numCourses:
            return res
        return []
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0] * numCourses
        adj_list = [[] for _ in range(numCourses)]

        for u, v in prerequisites:
            indegrees[v] += 1
            adj_list[u].append(v)

        queue = [i for i, x in enumerate(indegrees) if x == 0]

        while queue:
            curr = queue.pop()

            for a in adj_list[curr]:
                indegrees[a] -= 1
                if indegrees[a] == 0:
                    queue.append(a)

        if sum(indegrees) == 0:
            return True
        else:
            return False
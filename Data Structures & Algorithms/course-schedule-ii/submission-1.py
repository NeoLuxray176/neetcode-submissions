class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = [0] * numCourses
        al = [[] for _ in range(numCourses)]

        for u, v in prerequisites:
            al[v].append(u)
            indegrees[u] += 1

        queue = deque()

        for i in range(numCourses):
            if indegrees[i] == 0:
                queue.append(i)

        res = []
        
        while queue:
            u = queue.popleft()

            res.append(u)

            for v in al[u]:
                indegrees[v] -= 1
                if indegrees[v] == 0:
                    queue.append(v)

        print(indegrees)
        if len(res) == numCourses:
            return res
        
        return []
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Kahns algorithm for topological sorting
        # Compute the indegrees and an adjacency list

        indegrees = [0] * numCourses
        al = [[] for _ in range(numCourses)]

        for u, v in prerequisites:
            al[v].append(u)
            indegrees[u] += 1

        queue = deque()

        for i in range(numCourses):
            if indegrees[i] == 0:
                queue.append(i)
        
        finished = 0
        while queue:
            u = queue.popleft()

            finished += 1
            for v in al[u]:
                indegrees[v] -= 1
                if indegrees[v] == 0:
                    queue.append(v)


        return finished == numCourses
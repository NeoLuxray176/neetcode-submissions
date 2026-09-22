class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        al = [[] for _ in range(numCourses)]
        indegrees = [0] * numCourses

        for u, v in prerequisites:
            indegrees[v] += 1
            al[u].append(v)

        q = deque()
        for i in range(numCourses):
            if indegrees[i] == 0:
                q.append(i)
        
        finished = 0
        while q:
            u = q.popleft()
            finished += 1
            for v in al[u]:
                indegrees[v] -= 1
                if indegrees[v] == 0:
                    q.append(v)


        return finished == numCourses
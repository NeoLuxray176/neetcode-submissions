class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = [False] * n

        al = [[] for _ in range(n)]
        for u, v in edges:
            al[v].append(u)
            al[u].append(v)

        stack = [(0, -1)]

        res = 1
        has_unvisited_nodes = True

        while has_unvisited_nodes:

            while stack:
                node, prev = stack.pop()

                if visited[node]:
                    continue

                visited[node] = True

                for nei in al[node]:
                    if nei == prev:
                        continue
                    stack.append((nei, node))

            has_unvisited_nodes = False
            for i in range(n):
                if not visited[i]:
                    has_unvisited_nodes = True
                    res += 1
                    stack.append((i, -1))
                    break

        return res

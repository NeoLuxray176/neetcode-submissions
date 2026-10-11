class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj_list = [[] for _ in range(n)]

        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        stack = [0]
        visited = set()

        while stack:
            curr = stack.pop()

            if curr in visited:
                continue
            visited.add(curr)

            for v in adj_list[curr]:
                stack.append(v)

        return len(visited) == n


        

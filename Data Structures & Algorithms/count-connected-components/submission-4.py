class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Iterate over n
        # dfs starting at n
        # keep visited set to skip over nodes we have already seen

        adj_list = [[] for _ in range(n)]
        visited = set()
        res = 0

        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        for i in range(n):
            if i in visited:
                continue
            res += 1
            stack = [i]

            while stack:
                curr = stack.pop()

                for v in adj_list[curr]:
                    if v not in visited:
                        stack.append(v)
                        visited.add(v)

        return res
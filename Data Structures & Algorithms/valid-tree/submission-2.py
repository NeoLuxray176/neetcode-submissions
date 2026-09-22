class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visit = set()
        al = [[] for _ in range(n)]
        
        for u, v in edges:
            al[u].append(v)
            al[v].append(u)

        def dfs(node, par):
            if node in visit:
                return False

            visit.add(node)

            for v in al[node]:
                if v == par:
                    continue
                if not dfs(v, node):
                    return False

            return True

        return dfs(0, -1) and len(visit) == n
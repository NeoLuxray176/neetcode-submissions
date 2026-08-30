class Solution:
    def partition(self, s: str) -> List[List[str]]:
        m = len(s)
        def is_pali(cand : str) -> bool:
            n = len(cand)
            for i in range(n // 2):
                if cand[i] != cand[n - 1 - i]:
                    return False
            return True

        res, part = [], []

        def dfs(i : int, j : int):
            if j >= m:
                if i == j:
                    res.append(part.copy())
                return

            curr = s[i : j + 1]
            if is_pali(curr):
                part.append(curr)
                dfs(j + 1, j + 1)
                part.pop()
            
            dfs(i, j + 1)

        dfs(0, 0)
        return res
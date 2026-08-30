class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_pali(cand : str) -> bool:
            n = len(cand)
            for i in range(len(cand) // 2):
                if cand[i] != cand[n - 1 - i]:
                    return False
            return True

        res, part = [], []

        def dfs(i : int, j : int):
            if j >= len(s):
                if i == j:
                    res.append(part.copy())
                return

            if is_pali(s[i : j + 1]):
                part.append(s[i : j + 1])
                dfs(j + 1, j + 1)
                part.pop()
            
            dfs(i, j + 1)

        dfs(0, 0)
        return res
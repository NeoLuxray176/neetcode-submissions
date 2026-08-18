class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_pali(cand : str) -> bool:
            n = len(cand)
            for i in range(len(cand) // 2):
                if cand[i] != cand[n - 1 - i]:
                    return False
            return True

        res, part = [], []

        def dfs(j : int, i : int):
            if i >= len(s):
                if i == j:
                    res.append(part.copy())
                return

            if is_pali(s[j : i + 1]):
                part.append(s[j : i + 1])
                dfs(i + 1, i + 1)
                part.pop()
            
            dfs(j, i + 1)

        dfs(0, 0)
        return res
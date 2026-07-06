class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(start: int, total: int) -> None:
            if total == target:
                res.append(path.copy())
                return

            if total > target:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                dfs(i, total + candidates[i])   # reuse allowed
                path.pop()

        dfs(0, 0)
        return res
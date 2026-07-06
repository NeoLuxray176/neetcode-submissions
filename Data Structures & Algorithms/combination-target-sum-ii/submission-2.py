class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(idx, path, cur):
            if cur == target:
                res.append(path.copy())
                return
            for i in range (idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                if cur + candidates[i] > target:
                    break
                
                path.append(candidates[i])
                dfs(i+1, path, cur + candidates[i])
                path.pop()
                # We don't go into the left path again because we cannot
                # use a single entry twice
        
        dfs(0, [], 0)
        return res
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(start_index : int, curr_sum : int):
            if curr_sum == target:
                res.append(path.copy())
                return

            if curr_sum > target:
                return

            for i in range(start_index, len(candidates)):
                path.append(candidates[i])
                dfs(i, curr_sum + candidates[i])
                path.pop()
        
        dfs(0,0)
        return res
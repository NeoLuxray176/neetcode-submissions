class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curr_arr, curr_total):
            if curr_total == target:
                res.append(curr_arr.copy())
                return
            if i >= len(candidates) or curr_total > target:
                return

            curr_arr.append(candidates[i])
            dfs(i, curr_arr, curr_total + candidates[i])
            curr_arr.pop()
            dfs(i + 1, curr_arr, curr_total)

        dfs(0, [], 0)
        
        return res
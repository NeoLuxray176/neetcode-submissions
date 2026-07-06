class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(start : int, curr_total : int):
            if curr_total == target:
                res.append(path.copy())
                return

            if curr_total > target:
                return

            for i in range(start, len(nums)):
                path.append(nums[i])
                dfs(i, curr_total + nums[i])
                path.pop()

        
        dfs(0,0)
        return res
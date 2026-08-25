class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(nums: List[int], path : List[int], curr_sum : int):
            if curr_sum == target:
                res.append(path)
                return
            if curr_sum > target:
                return
            
            for i in range(len(nums)):
                num = nums[i]
                dfs(nums[i:], path + [num], curr_sum + num)
            return

        dfs(nums, [], 0)
        
        return res
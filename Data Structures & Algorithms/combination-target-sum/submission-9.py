class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # We can include every number as many times as we want
        # For each number we can decide to include it or to not include it
        # Binary tree where each node is the decision to include a number, children are sum with
        # that number included or that number excluded

        res = []
        # path = []

        def dfs(curr_sum : int, path : list, i : int):
            if curr_sum == target:
                res.append(path.copy())
                return
            
            if curr_sum > target or i >= len(nums):
                return
            
            
            path.append(nums[i])
            dfs(curr_sum + nums[i],path, i)
            path.pop()
            dfs(curr_sum,path, i+1)
                

        dfs(0, [], 0)
        return res
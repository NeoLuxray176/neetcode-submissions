class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        def dfs(i):
            if i >= n:
                return 0
            
            return max(nums[i] + dfs(i + 2), dfs(i + 1))

        return dfs(0)
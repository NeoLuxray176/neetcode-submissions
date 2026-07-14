class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        def dfs(i, nums):
            if i >= len(nums):
                return 0

            return max(dfs(i + 1, nums), nums[i] + dfs(i + 2, nums))

        return max(dfs(0, nums[1:]), dfs(1, nums[::]))
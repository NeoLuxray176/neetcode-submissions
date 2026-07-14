class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        cache = [-1] * n

        if n == 1:
            return nums[0]

        def dfs(i, nums):
            if i >= len(nums):
                return 0

            if cache[i] != -1:
                return cache[i]

            cache[i] = max(dfs(i + 1, nums), nums[i] + dfs(i + 2, nums))

            return cache[i]

        return max(dfs(0, nums[1:]), dfs(1, nums[::]))
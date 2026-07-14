class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        cache1 = [-1] * n
        cache2 = [-1] * n

        if n == 1:
            return nums[0]

        def dfs(i, nums, cache):
            if i >= len(nums):
                return 0

            if cache[i] != -1:
                return cache[i]

            cache[i] = max(dfs(i + 1, nums, cache), nums[i] + dfs(i + 2, nums, cache))

            return cache[i]

        return max(dfs(1, nums[::], cache1), dfs(0, nums[:n-1], cache2))
from functools import cache

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n

        for i in range(n - 1, -1, -1):
            for j in range(i, -1, -1):
                if nums[j] < nums[i]:
                    dp[j] = max(dp[j], 1 + dp[i])

        return max(dp)
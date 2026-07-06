class Solution:
    def rob(self, nums: List[int]) -> int:
        # At each house we can decide whether we'd like to rob this one
        # or maybe it would've been smarter to rob the previous one

        n = len(nums)
        dp = [0] * n

        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max((dp[i - 2] + nums[i], dp[i]))

        return dp[-1]
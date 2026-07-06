class Solution:
    def rob(self, nums: List[int]) -> int:
        # At each house we can decide whether we'd like to rob this one
        # or maybe it would've been smarter to rob the previous one

        n = len(nums)
        dp = [0] * n

        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max((dp[i - 2] + nums[i], dp[i-1]))

        return dp[-1]
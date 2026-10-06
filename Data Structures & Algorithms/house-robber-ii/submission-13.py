class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        dp = [0] * n
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, n - 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        a = dp[n - 2]

        dp[0], dp[1] = 0, nums[1]

        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        b = dp[n - 1]

        return max(a, b)



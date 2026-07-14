class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        dp = [0] * n
        # dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        dp[0], dp[1] = 0, max(0, nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        
        max1 = dp[n-1]

        dp = [0] * n
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        # dp[0], dp[1] = 0, max(0, nums[1])

        for i in range(2, n-1):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

        max2 = dp[n-2]

        return max(max1, max2)

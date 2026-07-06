class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        dp = [0] * n
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

        return dp[-1]
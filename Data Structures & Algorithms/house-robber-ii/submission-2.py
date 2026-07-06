class Solution:
    def rob(self, nums : List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        return max(self.help_rob(nums[1:]), self.help_rob(nums[:-1]))

    def help_rob(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [0] * n

        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])

        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[-1]
class Solution:
    def rob(self, nums: List[int]) -> int:
        # Idea calculate two results
        n = len(nums)

        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        return max(self.rob_internal(nums[1:]), self.rob_internal(nums[:n-1]))

    

    def rob_internal(self, nums : List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        dp = [0] * n
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[n - 1]
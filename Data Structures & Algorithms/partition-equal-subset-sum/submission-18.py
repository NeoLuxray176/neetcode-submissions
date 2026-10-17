class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        s = sum(nums)
        if s % 2 != 0:
            return False

        target = s // 2
        dp = [False] * (target + 1)
        dp[target] = True

        for i in range(target, -1, -1):
            for j in range(n):
                if i - nums[j] >= 0:
                    dp[i - nums[j]] = dp[i - nums[j]] or dp[i]

        return dp[0]
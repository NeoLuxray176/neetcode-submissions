from functools import cache

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False

        target = sum(nums) // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for i in range(target + 1):
            for num in nums:
                if i >= num:
                    dp[i] = dp[i] or dp[i - num]

        print(dp)
        return dp[target]




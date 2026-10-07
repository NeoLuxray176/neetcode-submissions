from functools import cache

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False

        target = sum(nums) // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            # If we went into the other direction then we might reuse our number
            # this way we only use it once
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]


        return dp[target]

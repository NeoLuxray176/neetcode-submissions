class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        s = sum(nums)
        if s % 2 != 0:
            return False

        target = s // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for i in range(target, -1, -1):
                if i + num < target + 1:
                    # print(f"Set {i + num} to {dp[i + num]} or {dp[i]}")
                    dp[i + num] = dp[i + num] or dp[i]

        
        print(dp)
        return dp[-1]
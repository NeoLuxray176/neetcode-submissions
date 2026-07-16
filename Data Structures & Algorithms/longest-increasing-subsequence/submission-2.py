class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        m = 1

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if nums[i] < nums[j]:
                    res = max(dp[i], dp[j] + 1)
                    dp[i] = res
                    m = max(res, m)

        return m
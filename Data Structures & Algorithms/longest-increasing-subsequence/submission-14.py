class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n

        # At each entry in dp store the longest increasing subsequence starting at that index
        # We start at the back where the value is 1
        # then for the next value we compare it to the largest length seen so far

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # We go from right to left
        # For each element we check all elements right to it
        # we count all elements larger than it and increase
        # our value to the maximum of the privous value stored here and the maximum stored at the larger element

        n = len(nums)
        dp = [1] * n

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)
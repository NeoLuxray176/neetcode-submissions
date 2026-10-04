from functools import cache

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def dfs(i : int) -> int:
            if i >= n:
                return 1
            
            best = 1
            for j in range(i, n):
                if nums[j] > nums[i]:
                    best = max(best, 1 + dfs(j))

            return best

        best = 0
        for i in range(n):
            best = max(best, dfs(i))

        return best
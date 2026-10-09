from functools import cache

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        
        @cache
        def backtrack(i : int) -> int:
            if i >= n:
                return 0

            res = 1
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    res = max(res, 1 + backtrack(j))

            return res

        res = 1
        for i in range(n):
            res = max(res, backtrack(i))

        return res

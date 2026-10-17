from functools import cache

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        cache = {}

        def recurse(start : int):
            if start >= n:
                return 0

            if start in cache:
                return cache[start]

            res = 1
            for j in range(start + 1, n):
                if nums[j] > nums[start]:
                    res = max(res, 1 + recurse(j))

            cache[start] = res
            return res

        res = 1
        for i in range(n):
            res = max(res, recurse(i))

        return res


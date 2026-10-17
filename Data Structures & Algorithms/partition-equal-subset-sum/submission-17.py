from functools import cache

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        s = sum(nums)
        if s % 2 != 0:
            return False

        target = s // 2

        @cache
        def backtrack(curr_sum : int, start_index : int) -> bool:
            if curr_sum == target:
                return True
            if start_index >= n:
                return False

            res = False
            res = res or backtrack(curr_sum + nums[start_index], start_index + 1)
            res = res or backtrack(curr_sum, start_index + 1)

            return res

        if backtrack(0, 0):
            return True
        else:
            return False
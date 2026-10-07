from functools import cache

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False

        target = sum(nums) // 2

        @cache
        def backtrack(curr_sum : int, index : int) -> bool:
            if curr_sum > target:
                return False
            if curr_sum == target:
                return True
            if index >= len(nums):
                return False

            a = backtrack(curr_sum + nums[index], index + 1)
            b = backtrack(curr_sum, index + 1)

            return a or b

        return backtrack(0, 0)


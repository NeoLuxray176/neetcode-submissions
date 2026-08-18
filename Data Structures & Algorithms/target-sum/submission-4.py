class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def backtrack(i, total):
            if i == len(nums):
                return total == target

            if (i, total) in dp:
                return dp[(i, total)]

            res = (backtrack(i + 1, total + nums[i])) + backtrack(i + 1, total - nums[i])

            dp[(i, total)] = res

            return res

        return backtrack(0, 0)
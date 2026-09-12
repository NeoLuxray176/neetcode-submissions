class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Can we think of this as a decision tree?
        # For each number in nums we can either use it for our sum
        # or not use it. Then we could create a sort of recursive DFS solution.

        res = []

        def backtrack(j : int, curr : List[int], curr_sum : int) -> List[int]:
            if curr_sum == target:
                res.append(curr)
                return
            if curr_sum > target:
                return

            for i in range(j, len(nums)):
                backtrack(i, curr + [nums[i]], curr_sum + nums[i])

        backtrack(0, [], 0)
        return res

            
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def backtrack(path : List[int], curr_sum : int, index : int):
            if curr_sum > target:
                return

            if curr_sum == target:
                res.append(path[::])
                return

            if index >= len(nums):
                return

            backtrack(path + [nums[index]], curr_sum + nums[index], index)
            backtrack(path, curr_sum, index + 1)

        backtrack([], 0, 0)
        return res

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = []

        def backtrack(path : List[int], curr_sum : int, start : int):
            if curr_sum > target:
                return
            if start >= n:
                return
            if curr_sum == target:
                res.append(path[::])
                return

            path.append(nums[start])
            backtrack(path, curr_sum + nums[start], start)
            path.pop()
            backtrack(path, curr_sum, start + 1)
            return

        backtrack([], 0, 0)
        return res
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)

        res = []

        def backtrack(path : List[int], ind : int, curr_sum : int):
            if curr_sum == target:
                res.append(path[::])
                return

            if curr_sum > target:
                return

            if ind >= n:
                return

            path.append(nums[ind])
            backtrack(path, ind, curr_sum + nums[ind])
            path.pop()
            backtrack(path, ind + 1, curr_sum)
            return

        backtrack([], 0, 0)

        return res
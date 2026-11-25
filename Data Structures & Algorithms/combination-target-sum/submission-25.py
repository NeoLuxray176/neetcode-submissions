class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)

        res = []

        def backtrack(start : int, curr_sum : int, path : List[int]):
            if curr_sum == target:
                res.append(path[::])
                return
            if curr_sum > target:
                return
            if start >= n:
                return

            path.append(nums[start])
            backtrack(start, curr_sum + nums[start], path)
            path.pop()
            backtrack(start + 1, curr_sum, path)

        backtrack(0, 0, [])

        return res
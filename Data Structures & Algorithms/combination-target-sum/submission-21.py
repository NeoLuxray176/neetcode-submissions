class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)

        def backtrack(start : int, path : List[int], curr_sum : int):
            if curr_sum > target:
                return
            if curr_sum == target:
                res.append(path[::])
                return
            if start >= n:
                return

            path.append(nums[start])
            backtrack(start, path, curr_sum + nums[start])
            path.pop()
            backtrack(start + 1, path, curr_sum)
            return

        backtrack(0, [], 0)
        return res
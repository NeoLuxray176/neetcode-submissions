class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = []

        nums.sort()

        def backtrack(i : int, path : List[int], curr_sum : int):
            if curr_sum == target:
                res.append(path[::])
                return

            if curr_sum > target:
                return

            if i >= n:
                return

            path.append(nums[i])
            backtrack(i, path, curr_sum + nums[i])
            path.pop()
            backtrack(i + 1, path, curr_sum)
            return

        backtrack(0, [], 0)

        return res
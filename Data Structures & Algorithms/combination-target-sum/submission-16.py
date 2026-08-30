class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)

        res = []

        def dfs(path : List[int], curr_nums : List[int], curr_sum : int):
            if curr_sum == target:
                res.append(path.copy())
                return

            if curr_sum > target:
                return

            for i in range(len(curr_nums)):
                num = curr_nums[i]
                # Take this number
                dfs(path + [num], curr_nums[i:], curr_sum + num)

        dfs([], nums, 0)

        return res
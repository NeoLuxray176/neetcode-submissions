class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(i : int, path : List[int]):
            if i >= len(nums):
                res.append(path[::])
                return

            backtrack(i + 1, path + [nums[i]])
            j = i + 1
            while j < len(nums) and nums[i] == nums[j]:
                j += 1
            backtrack(j, path)

        backtrack(0, [])
        return res
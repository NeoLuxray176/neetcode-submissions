class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)

        res = []

        def backtrack(path : List[int], index : int):
            if index == n:
                res.append(path[::])
                return

            path.append(nums[index])
            backtrack(path, index + 1)
            path.pop()

            curr = nums[index]
            while index < n and curr == nums[index]:
                index += 1
            backtrack(path, index)
            return

        backtrack([], 0)
        return res

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()

        res = []
        used = [False] * n

        def backtrack(path : List[int]):
            if len(path) == n:
                res.append(path[::])

            for i in range(n):
                if used[i]:
                    continue
                if i > 0 and used[i - 1] and nums[i] == nums[i - 1]:
                    continue

                path.append(nums[i])
                used[i] = True
                backtrack(path)
                used[i] = False
                path.pop()
            return

        backtrack([])
        return res

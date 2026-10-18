class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        

        used = [False] * n
        res = []

        def backtrack(start : int, path : List[int]):
            if len(path) == n:
                res.append(path[::])
                return

            for i in range(n):
                if used[i]:
                    continue

                if i > 0 and nums[i] == nums[i - 1] and used[i - 1]:
                    continue

                path.append(nums[i])
                used[i] = True
                backtrack(i, path)
                path.pop()
                used[i] = False

        backtrack(0, [])

        return res
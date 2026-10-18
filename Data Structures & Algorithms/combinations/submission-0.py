class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = list(range(1, n + 1))
        res = []

        def backtrack(start : int, path : List[int]):
            if len(path) == k:
                res.append(path[::])
                return

            for i in range(start, n):
                print(i, len(nums))
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
            return

        backtrack(0, [])
        return res
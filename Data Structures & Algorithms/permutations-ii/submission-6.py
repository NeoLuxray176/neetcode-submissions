class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        counts = Counter(nums)
        res = []

        def backtrack(path : List[int]):
            if len(path) == n:
                res.append(path[::])
                return

            for num in counts:
                if counts[num] > 0:
                    counts[num] -= 1
                    path.append(num)
                    backtrack(path)
                    path.pop()
                    counts[num] += 1
        
        backtrack([])
        return res
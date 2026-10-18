class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]

        curr = nums[0]
        prevs = self.permuteUnique(nums[1:])
        res = []

        for prev in prevs:
            for i in range(len(prev) + 1):
                new = prev[:i] + [curr] + prev[i:]
                if res and res[-1] == new:
                    continue
                res.append(prev[:i] + [curr] + prev[i:])

        return res
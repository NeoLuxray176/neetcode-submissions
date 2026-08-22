class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        if n == 0:
            return []

        if n == 1:
            return [nums]

        res = []
        
        curr = nums[0]
        rest = nums[1:]
        prevs = self.permute(rest)

        for prev in prevs:
            for i in range(len(prev) + 1):
                res.append(prev[:i] + [curr] + prev[i:])

        return res
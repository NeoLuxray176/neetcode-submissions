class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]

        curr = nums[0]
        prevs = self.subsets(nums[1:])

        res = prevs.copy()
        for prev in prevs:
            res.append(prev + [curr])

        return res
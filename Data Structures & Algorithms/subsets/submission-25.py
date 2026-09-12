class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]

        curr = nums[0]
        prevs = self.subsets(nums[1:])

        new = []
        for prev in prevs:
            new.append(prev + [curr])

        return prevs + new
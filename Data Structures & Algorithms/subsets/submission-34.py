class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]

        curr = nums[0]
        prevs = self.subsets(nums[1:])

        news = []

        for prev in prevs:
            adding = prev[::] + [curr]
            news.append(adding)

        return prevs + news
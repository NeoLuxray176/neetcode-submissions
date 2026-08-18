class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # the first item needs to be at every possible position
        # So we could try to build this from an empty array
        # insert 1 [1]
        # Now we look at the next item, we need to insert it at every possible index
        # that is index 0 and index 1
        # We get [1, 2] and [2, 1]
        # Now let's look at the next item, we need to insert it at every possible index
        # that is indices 0, 1, 2

        n = len(nums)

        if n == 0:
            return []

        if n == 1:
            return [nums]

        curr = nums[0]
        prevs = self.permute(nums[1:])
        res = []

        for prev in prevs:
            for i in range(len(prev) + 1):
                res.append(prev[:i] + [curr] + prev[i:])

        return res
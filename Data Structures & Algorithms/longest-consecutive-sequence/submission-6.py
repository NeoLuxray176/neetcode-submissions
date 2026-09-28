class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        best = 1

        for num in nums:
            if num - 1 not in nums_set:
                i = 1
                while num + i in nums_set:
                    i += 1
                best = max(i, best)

        return best
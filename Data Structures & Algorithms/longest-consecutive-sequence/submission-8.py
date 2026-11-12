class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        res = 1

        for num in nums:
            if num - 1 not in nums_set:
                curr = num
                while curr in nums_set:
                    res = max(res, curr - num + 1)
                    curr += 1

        return res
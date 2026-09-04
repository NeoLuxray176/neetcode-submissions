class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums_set = set(nums)

        res = 0

        for num in nums:
            if num - 1 not in nums_set:
                # This is the start of a sequence
                curr = num
                streak = 0
                while curr in nums_set:
                    streak += 1
                    curr += 1
                res = max(res, streak)

        return res
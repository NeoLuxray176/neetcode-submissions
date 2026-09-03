class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        res = 1

        for num in nums:
            if num - 1 not in nums_set:
                seq = num
                curr = 0
                while seq in nums_set:
                    seq += 1
                    curr += 1
                res = max(curr, res)

        return res
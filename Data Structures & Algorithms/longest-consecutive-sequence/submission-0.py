class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_length = 0

        for i in range(len(nums)):
            if (nums[i] - 1) not in nums_set:
                length = 0
                curr = nums[i]
                while curr in nums_set:
                    curr += 1
                    length += 1

                max_length = max(max_length, length)
        return max_length

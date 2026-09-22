class Solution:
    def canJump(self, nums: List[int]) -> bool:
        end = 0

        for i, num in enumerate(nums):
            if i > end:
                return False
            end = max(end, i + num)

        return end >= len(nums) - 1
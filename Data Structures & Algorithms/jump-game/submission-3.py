class Solution:
    def canJump(self, nums: List[int]) -> bool:
        end = 0

        for i, num in enumerate(nums):
            if i > end:
                return False
            # print(end, i + num)
            end = max(end, i + num)

        # print(end, len(nums))
        return end >= len(nums) - 1
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0

        for i, num in enumerate(nums):
            if farthest < i:
                return False
            
            farthest = max(farthest, i + num)

        return True

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        next_insert = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[next_insert], nums[i] = nums[i], nums[next_insert]
                next_insert += 1
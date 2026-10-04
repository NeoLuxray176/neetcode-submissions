class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 0

        while i < len(nums):
            if nums[i] == 0:
                j = i
                while j < len(nums) - 1 and nums[j] == 0:
                    j += 1
                # print(f"Swap {i} and {j}")
                nums[i] = nums[j]
                nums[j] = 0
            i += 1
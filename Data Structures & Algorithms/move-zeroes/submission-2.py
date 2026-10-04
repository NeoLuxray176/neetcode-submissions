class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        next_nonzero = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                # Place this nonzero after the nonzeros already processed.
                nums[next_nonzero], nums[i] = nums[i], nums[next_nonzero]
                next_nonzero += 1
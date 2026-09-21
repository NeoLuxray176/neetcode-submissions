class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 0

        while j < len(nums):
            if j > 0 and nums[j] == nums[j - 1]:
                j += 1
            else:
                nums[i] = nums[j]
                i += 1
                j += 1

        return i
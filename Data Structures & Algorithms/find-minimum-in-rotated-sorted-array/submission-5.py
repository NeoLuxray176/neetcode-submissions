class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            middle = (left + right) // 2

            if nums[middle] < nums[right]:
                # We are in the sorted part of the array, the minimum
                # is therefore left of the right border
                right = middle
            else:
                # We are not in the sorted part of the array, the minimum
                # is therefore to the right of the left border
                left = middle + 1

        return nums[left]
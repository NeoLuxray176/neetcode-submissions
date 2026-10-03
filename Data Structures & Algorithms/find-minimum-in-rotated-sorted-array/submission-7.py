class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] < nums[-1]:
                # We are in the sorted part
                right = middle - 1
            else:
                # We are in the unsorted part
                left = middle + 1

        return nums[left]
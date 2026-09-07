class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        left, right = 0, n - 1

        while left < right:
            middle = (left + right) // 2

            if nums[middle] < nums[right]:
                right = middle
            else:
                left = middle + 1

        return nums[left]
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # The idea is that we check against target and then depending on whether
        # we're in the sorted or unsorted part we adjust left or right or vice versa
        left, right = 0, len(nums) - 1

        while left < right:
            middle = (left + right) // 2

            if nums[middle] == target:
                return middle
            if nums[middle] <= nums[right]:
                # we are in the sorted part of the array
                if nums[middle] < target:
                    left = middle + 1
                else:
                    right = middle - 1
            else:
                if nums[middle] < target:
                    right = middle - 1
                else:
                    left = middle + 1

        return -1
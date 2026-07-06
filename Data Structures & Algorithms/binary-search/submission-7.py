class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # We want to look at the middle value if it is larger than target
        # go to the left half; if it is smaller than the target value go to the right half
        # and look at the middle point for each of the halves.
        # This will half our search space in each iteration giving us logarithmic runtime

        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            else: # nums[middle] > target
                right = middle - 1
        
        return -1 

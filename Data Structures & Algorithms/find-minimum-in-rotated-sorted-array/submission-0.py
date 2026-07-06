class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            middle = (l + r) // 2

            if nums[middle] < nums[r]:
                # We are in the sorted part of the array
                # the minimum is in the left half
                r = middle
            else: # nums[middle] >= nums[r]
                # We are in the right half of the array
                l = middle + 1
        
        return nums[l] 
        
                

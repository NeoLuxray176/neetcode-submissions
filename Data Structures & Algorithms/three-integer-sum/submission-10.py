class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the nums array
        # then we can fix one of the numbers and check all other values with a two pointer approach
        # We need to make sure that the output does not contain any duplicates. We can avoid
        # duplicates by checking that the fixed number is not equal to the previosu fixed number

        res = []

        nums.sort()

        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, n - 1
            while left < right:
                curr = nums[i] + nums[left] + nums[right]
                if curr == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif curr < 0:
                    left += 1
                else:
                    right -= 1
        
        return res

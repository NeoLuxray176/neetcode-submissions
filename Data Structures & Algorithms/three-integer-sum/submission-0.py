class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        nums.sort()
        
        for i, a in enumerate(nums):
            # We require the i component to be negative
            if a > 0:
                break
            
            # This is a duplicate
            if i > 0 and a == nums[i - 1]:
                continue

            l = i + 1
            r = n - 1
            while l < r:
                threeSum = a + nums[l] +  nums[r]

                if threeSum > 0:
                    r -= 1
                if threeSum < 0:
                    l += 1
                if threeSum == 0:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
            
        return res
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # This is Kadanes algorithm

        n = len(nums)

        res = nums[0]
        currMin, currMax = 1, 1
         
        for num in nums:
            a,b,c = num * currMax, num * currMin, num
            currMax = max(a, b ,c)
            currMin = min(a, b ,c)
            res = max(res, currMax)

        return res
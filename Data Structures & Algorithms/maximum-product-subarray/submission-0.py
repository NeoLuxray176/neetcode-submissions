class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        currMin, currMax = 1, 1

        for num in nums:
            tmp = currMax * num
            currMax = max(currMax * num, num * currMin, num)
            currMin = min(tmp, num * currMin, num)
            res = max(res, currMax)

        return res
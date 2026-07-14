class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # The value of the maximum subarray always increases unless we add a negative number
        # Only when the current candidate for a max subarray starts being negative

        maxSub, curSum = nums[0], 0
        for num in nums:
            if curSum < 0:
                curSum = 0
            curSum += num
            maxSub = max(maxSub, curSum)
        return maxSub
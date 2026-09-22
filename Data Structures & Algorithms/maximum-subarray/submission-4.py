class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = 0

        for num in nums:
            res = max(num, res + num)

        return res
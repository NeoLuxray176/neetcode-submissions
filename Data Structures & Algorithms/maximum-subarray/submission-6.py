class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float("-inf")
        curr = float("-inf")

        for num in nums:
            curr = max(curr + num, num)
            res = max(res, curr)

        return res
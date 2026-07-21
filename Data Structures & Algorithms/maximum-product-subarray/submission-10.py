class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minRes = 1
        maxRes = 1

        res = nums[0]

        for num in nums:
            a = minRes * num
            b = maxRes * num
            minRes = min(num, a, b)
            maxRes = max(num, a, b)
            # print(maxRes)

            res = max(res, maxRes)

        return res
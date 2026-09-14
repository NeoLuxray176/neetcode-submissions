class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curr_min, curr_max = 1, 1

        for num in nums:
            tmp = curr_max * num
            curr_max = max(num * curr_max, num * curr_min, num)
            curr_min = min(tmp, num * curr_min, num)
            res = max(res, curr_max)

        return res
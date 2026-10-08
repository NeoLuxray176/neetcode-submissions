class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = 1
        curr_min = 1
        res = float("-inf")

        for num in nums:
            temp_max = max(num, curr_max * num, curr_min * num)
            curr_min = min(num, curr_max * num, curr_min * num)
            curr_max = temp_max

            res = max(res, curr_max)


        return res
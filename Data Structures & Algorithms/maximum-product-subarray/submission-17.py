class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = 1
        curr_min = 1
        res = float("-inf")

        for num in nums:
            curr_max = max(num, curr_max * num, curr_min * num)
            curr_min = min(curr_max * num, curr_min * num)

            res = max(res, curr_max)
            # print(res, curr_max, curr_min)

        return res
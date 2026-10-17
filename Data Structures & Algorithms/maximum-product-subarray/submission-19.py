class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product, min_product = 1, 1
        res = float("-inf")

        for num in nums:
            max_product = max(max_product * num, min_product * num, num)
            min_product = min(max_product * num, min_product * num, num)
            
            res = max(res, max_product)

        return res
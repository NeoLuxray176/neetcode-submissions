class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product, min_product = 1, 1
        res = float("-inf")

        for num in nums:
            a, b, c = max_product * num, min_product * num, num
            max_product, min_product = max(a, b, c), min(a, b, c)
            
            res = max(res, max_product)

        return res
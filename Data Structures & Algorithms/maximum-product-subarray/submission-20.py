class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product, min_product = 1, 1
        res = float("-inf")

        for num in nums:
            tmp = max_product
            max_product = max(max_product * num, min_product * num, num)
            min_product = min(tmp * num, min_product * num, num)
            
            res = max(res, max_product)

        return res
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_product = [1] * n
        suffix_product = [1] * n
        for i in range(1, n):
            prefix_product[i] = prefix_product[i - 1] * nums[i - 1]
            
        for i in range(1, n):    
            suffix_product[(n-1) - i] = suffix_product[(n-1) - i + 1] * nums[(n-1) - i + 1]

        output = [0] * n
        for i in range(n):
            output[i] = prefix_product[i] * suffix_product[i] 

        print(f"{prefix_product}")
        print(f"{suffix_product}")
        return output
        
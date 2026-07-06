class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1
                continue
            total_product *= num
        
        if zero_count > 1:
            return [0] * len(nums)

        output = [0] * len(nums)

        for i, num in enumerate(nums):
            if nums[i] == 0:
                output[i] = total_product
            
            if zero_count == 0: 
                output[i] = int(total_product / nums[i])

        return output

        
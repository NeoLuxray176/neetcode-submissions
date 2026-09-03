class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        prod = 1
        count_zeros = 0

        for num in nums:
            if num != 0:
                prod *= num
            else:
                count_zeros += 1
        
        res = [prod] * n

        if count_zeros > 1:
            return [0] * n

        for i in range(n):
            if count_zeros == 1:
                if nums[i] == 0:
                    res[i] = prod
                else:
                    res[i] = 0
            else:
                res[i] = res[i] // nums[i]

        return res

        

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # If all numbers were positive, then the maximum product would be the subarray without the zeros
        # If all numbers were negative, then the maximum product would be the subarray without the zeros

        # We get a positive number by multiplying two negative numbers, 
        # so by keeping the minimum value and the maximum value. We get the potential maximum value


        res = nums[0]
        minVal = 1
        maxVal = 1

        for num in nums:
            a = maxVal * num
            b = minVal * num


            minVal = min(num, a, b)
            maxVal = max(num, a, b)
            
            res = max(res, maxVal)

        return res
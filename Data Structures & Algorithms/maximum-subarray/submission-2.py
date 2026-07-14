class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # The value of the maximum subarray always increases unless we add a negative number
        # Only when the current candidate for a max subarray starts being negative

        max_subbarray_val = float("-inf")
        curr_max = float("-inf")

        for num in nums:
            curr_max += num
            
            curr_max = max(num, curr_max)
            max_subbarray_val = max(max_subbarray_val, curr_max)
            

        return max_subbarray_val
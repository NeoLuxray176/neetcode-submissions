class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        # Task: Given an array nums of positive integers, find the number of subarrays whose product is smaller than k
        # Constraints: positive integers
        # General Idea: Two pointers given a right pointer expand left until we exceed k. Note that the subarray only ever increaess
        # Refined Idea:
        # integer variable to store the result
        # left pointer
        # for start in right pointer: O(n)
        # variable curr product initially 1
        # expand left while left > 0 and curr product is smaller than k O(n) -> O(n^2) worst case
        # increment result variable since we have a new subarray
        # That is it.
        # Test Vectors:
        # [2, 3, 10] k 31

        n = len(nums)
        res, left, curr = 0, 0, 1

        for right in range(n):
            curr *= nums[right]
            
            while left <= right and curr >= k:
                curr //= nums[left]
                left += 1

            res += right - left + 1

        return res
                

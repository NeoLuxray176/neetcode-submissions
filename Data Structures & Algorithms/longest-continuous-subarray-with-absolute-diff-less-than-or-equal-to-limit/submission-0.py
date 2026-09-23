class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # Task
        # Return the length of the longest non-empty subarray so that the absolute difference between any two elements is less than limit

        # Constraints
        # The numbers are positive integers
        # Anything in terms of input size that I should be aware of?
        # Nothing

        # General Idea
        # Brute force
        # Check every subarray and keep track of its min and max element
        # This is O(n^2) operations
        # We can cache the results for intermediary subarrays so for example
        # subarray 3:5 needs to be computed for the subarray 1:6 but also for the subarray 3:7.

        # Idea:
        # Recursively compute the different subarrays and cache intermediary results
        # Start with subarray 0:1, then 0:2, then 0:4. Iterate over end points
        # For each of these recurse to smaller intermediary problems

        # 1. For every possible starting point of a subarray
        # 2. Compute the minimum and maximum element
        # 3. These are the min/max of the current element as well as the min/max element from the subarray i+1:j for all j
        
        n = len(nums)
        best = 0

        for i in range(n):
            curr_min, curr_max = nums[i], nums[i]
            for j in range(i, n):
                curr_min = min(curr_min, nums[j])
                curr_max = max(curr_max, nums[j])
                if abs(curr_max - curr_min) <= limit:
                    best = max(best, j - i + 1)
                else:
                    break

        return best






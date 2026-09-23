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
        l = res = 0

        min_q = deque()
        max_q = deque()

        for right in range(len(nums)):
            while min_q and nums[right] < min_q[-1]:
                min_q.pop()
            while max_q and nums[right] > max_q[-1]:
                max_q.pop()

            min_q.append(nums[right])
            max_q.append(nums[right])

            while max_q[0] - min_q[0] > limit:
                if nums[l] == max_q[0]:
                    max_q.popleft()
                if nums[l] == min_q[0]:
                    min_q.popleft()
                l += 1

            res = max(res, right - l + 1)

        return res





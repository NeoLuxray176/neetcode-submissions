class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        left = 0

        for right, value in enumerate(nums):
            if right - left > k:
                window.remove(nums[left])
                left += 1
            
            # We have found a duplicate and since window never contains
            # more than the last k elements, this is at most k elements away
            if value in window:
                return True

            window.add(value)

        return False
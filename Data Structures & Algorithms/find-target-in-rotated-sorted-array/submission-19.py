class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] == target:
                return middle

            # With distinct values, at least one half is sorted.
            if nums[middle] <= nums[right]:
                # The right half [middle, right] is sorted.
                if nums[middle] < target <= nums[right]:
                    # Target is within its range: search right.
                    left = middle + 1
                else:
                    # Target cannot be in the right half: search left.
                    right = middle - 1
            else:
                # The right half contains the rotation break,
                # so the left half [left, middle] is sorted.
                if nums[left] <= target < nums[middle]:
                    # Target is within its range: search left.
                    right = middle - 1
                else:
                    # Target cannot be in the left half: search right.
                    left = middle + 1

        # The search range is empty, so the target is absent.
        return -1
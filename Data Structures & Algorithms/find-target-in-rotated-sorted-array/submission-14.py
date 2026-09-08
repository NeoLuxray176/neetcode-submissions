class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # 1. Check middle.
        # 2. Determine which half is sorted.
        # 3. Check whether target lies inside that sorted half.
        # 4. If yes → search it.
        # 5. If no  → search the other half.

        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] == target:
                return middle

            if nums[middle] <= nums[right]:
                # The right half [middle, right] is sorted
                if nums[middle] < target <= nums[right]:
                    # The value is in the right half of the current scope
                    left = middle + 1
                else:
                    # The value is in the left half of the current scope
                    right = middle - 1
            else:
                # The left half [left, middle] is sorted
                if nums[left] <= target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1

        return -1
            
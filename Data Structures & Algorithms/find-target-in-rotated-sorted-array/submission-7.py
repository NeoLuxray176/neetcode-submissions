class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        middle = 0

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] == target:
                return middle

            if nums[middle] <= nums[right]:
                # Right half is sorted
                if nums[middle] < target <= nums[right]:
                    # print(f"Solution is in {nums[:middle]}")
                    left = middle + 1
                else:
                    print(f"Solution is in {nums[middle + 1:]}")
                    right = middle - 1
            else:
                # Left half is sorted
                if nums[left] <= target < nums[middle]:
                    # print(f"Solution is in {nums[:middle]}")
                    right = middle - 1
                else:
                    # print(f"Solution is in {nums[middle:]}")
                    left = middle + 1
        
        return middle if nums[middle] == target else -1
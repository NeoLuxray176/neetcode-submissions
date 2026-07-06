class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        middle = 0

        while left < right:
            middle = (left + right) // 2

            if nums[middle] == target:
                return middle

            if nums[middle] < nums[right]:
                # Right half is sorted
                if nums[middle] > target:
                    # print(f"Solution is in {nums[:middle]}")
                    right = middle
                else:
                    # print(f"Solution is in {nums[middle:]}")
                    left = middle + 1
            else:
                # Left half is sorted
                if nums[middle] < target:
                    # print(f"Solution is in {nums[:middle]}")
                    right = middle
                else:
                    # print(f"Solution is in {nums[middle:]}")
                    left = middle + 1
        
        return middle if nums[middle] == target else -1
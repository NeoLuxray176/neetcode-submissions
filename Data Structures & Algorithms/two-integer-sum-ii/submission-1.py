class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # non-decreasing order
        # means increasing order
        # left is small, right is large

        n = len(numbers)
        left, right = 0, n  - 1

        while left < right:
            curr_res = numbers[left] + numbers[right]
            if curr_res == target:
                return [1 + left, 1 + right]

            if curr_res < target:
                left += 1
            if curr_res > target:
                right -= 1


            
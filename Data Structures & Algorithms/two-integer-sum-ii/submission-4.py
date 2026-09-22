class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left, right = 0, n -1
        
        while left <= right:
            curr_sum = numbers[left] + numbers[right]
            if curr_sum == target:
                return [numbers[left], numbers[right]]
            elif curr_sum < target:
                left += 1
            else:
                right -= 1

        return [-1, -1]
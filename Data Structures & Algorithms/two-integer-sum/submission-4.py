class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}

        for i, num in enumerate(nums):
            if num in dictionary:
                return [dictionary[num], i]
            else:
                dictionary[target - num] = i

        return [-1, -1]
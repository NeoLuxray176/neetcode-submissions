class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return nums

        smallest = largest = best = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            candidates = (num, smallest * num, largest * num)
            smallest, largest = min(candidates), max(candidates)
            best = max(best, largest)

        return best
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        smallest = largest = best = nums[0]

        for num in nums[1:]:
            candidates = (num, num * smallest, num * largest)
            smallest = min(candidates)
            largest = max(candidates)
            best = max(best, largest)

        return best
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # We know that two numbers that have the same remainder differ by a multiple of k
        # So if the sum up to i has remainder r and the sum up to j also has remainder r. Then
        # the sum i to j is a multiple of K.

        hmap = {0 : -1}
        total = 0

        for i, num in enumerate(nums):
            total += num
            r = total % k
            if r not in hmap:
                hmap[r] = i
            elif i - hmap[r] >= 2:
                return True

        return False

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, min(n, i + 1 + k)):
                if nums[i] == nums[j] and abs(i - j) <= k:
                    return True

        return False
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort(reverse=True)

        for i in range(n):
            if nums[i] < i + 1:
                if nums[i] == i:
                    return -1
                else:
                    return i

        return i + 1
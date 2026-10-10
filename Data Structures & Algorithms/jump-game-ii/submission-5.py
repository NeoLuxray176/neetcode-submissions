class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest = 0
        curr = 0
        count = 0

        for i in range(len(nums) - 1):
            curr = max(curr, i + nums[i])

            if i == farthest:
                count += 1
                farthest = curr

        return count

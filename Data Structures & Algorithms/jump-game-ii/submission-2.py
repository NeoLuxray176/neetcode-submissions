class Solution:
    def jump(self, nums: List[int]) -> int:
        no_jumps = 0
        end = farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if end == i:
                no_jumps += 1
                end = farthest

        return no_jumps
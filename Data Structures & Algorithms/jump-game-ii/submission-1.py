class Solution:
    def jump(self, nums: List[int]) -> int:
        no_jumps = -1
        end = farthest = 0

        for i, num in enumerate(nums):
            farthest = max(farthest, i + num)
            if end == i:
                no_jumps += 1
                end = farthest

        return no_jumps
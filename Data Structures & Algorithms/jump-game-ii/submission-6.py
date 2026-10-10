class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest = 0
        curr = 0
        count = 0

        for i, num in enumerate(nums[:-1]):
            curr = max(curr, i + num)

            if i == farthest:
                count += 1
                farthest = max(farthest, curr)

        return count
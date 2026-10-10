class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest = nums[0]
        curr = nums[0]
        count = 0

        for i in range(1, len(nums)):
            curr = max(curr, i + nums[i])

            if i == farthest:
                count += 1
                farthest = curr
                curr = 0

        return count

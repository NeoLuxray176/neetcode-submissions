class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Does reach mean that we can overshoot the target?
        # We could try to start

        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1 , -1):
            if (goal - i) <= nums[i]: # Can jump a distance of i from nums[i]
                goal = i

        return goal == 0
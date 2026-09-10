class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, nums[0]

        while slow != fast:
            # print(f"{slow} {fast}")
            slow, fast = nums[slow], nums[nums[fast]]
            # print(f"{slow} {fast}")

        return nums[slow]
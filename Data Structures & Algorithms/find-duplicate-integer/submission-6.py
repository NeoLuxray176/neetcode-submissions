class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                return nums[slow]
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0

        # Phase 1: find a meeting point somewhere in the cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        # Phase 2: find the entrance to the cycle
        slow2 = 0

        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        put, take = 0, 0

        while take < len(nums):
            if nums[take] == val:
                take += 1
            else:
                nums[put] = nums[take]
                put += 1
                take += 1


        return put
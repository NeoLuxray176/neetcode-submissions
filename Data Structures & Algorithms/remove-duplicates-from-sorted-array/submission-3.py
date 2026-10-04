class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        put, get = 0, 0

        while get < len(nums):
            if get > 0 and nums[get] == nums[get - 1]:
                get += 1
            else:
                nums[put] = nums[get]
                get += 1
                put += 1

        return put
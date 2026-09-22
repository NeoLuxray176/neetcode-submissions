class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        put = 0

        for num in nums:
            if num != val:
                nums[put] = num
                put += 1

        return put
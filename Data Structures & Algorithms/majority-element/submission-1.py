class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elem, count = -1000000000 - 1, 0

        for num in nums:
            if elem == nums:
                count += 1
            else:
                count -= 1
            
            if count <= 0:
                elem = num
                count = 1

        return elem


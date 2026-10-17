class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elem, occ = float("-inf"), 0

        for num in nums:
            if num == elem:
                occ += 1
            else:
                occ -= 1

            if occ <= 0:
                elem, occ = num, 1

        return elem
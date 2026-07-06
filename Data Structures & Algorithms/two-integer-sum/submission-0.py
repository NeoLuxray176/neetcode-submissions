class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for i in nums:
            val = target - i
            if val in my_dict:
                return list[i, my_dict[val]]
            else:
                my_dict[val] = i
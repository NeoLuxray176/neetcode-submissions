class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # We start out with an empty set
        # For every num in nums, we append it to the previous solution
        # and add all these new entries to our solution

        if not nums:
            return [[]]

        curr = nums[0]
        res = self.subsets(nums[1:])

        print(res)

        new = []
        for re in res:
            arr = re.copy()
            arr.append(curr)
            new.append(arr)
        
        return res + new
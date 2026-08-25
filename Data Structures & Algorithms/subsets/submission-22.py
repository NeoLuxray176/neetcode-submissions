class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # example [1, 2, 3]
        # Start with the base case [[]]
        # For each of the inputs
        # add 1 to all existing values in the solution
        # append to solution


        res = [[]]

        for num in nums:
            tmp = []
            for re in res:
                tmp += [re + [num]]

            res += tmp

        return res
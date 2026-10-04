class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        curr = [[]]

        for num in nums:
            next_subsets = curr.copy()
            for subset in curr:
                next_subsets.append(subset + [num])
            curr = next_subsets

        return curr
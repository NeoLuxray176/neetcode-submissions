class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Could we try something recursive?

        # Base case [[]]
        # Alt base case [1] -> [[1]]
        # Insert at every position, iterate over all positions for every previous result
        # [1, 2] and prev result [1] then insert [2, 1] and [1, 2]

        if not nums:
            return [[]]

        curr = nums[0]
        prevs = self.permute(nums[1:]) # List[List[int]]

        res = []
        for prev in prevs:
            for i in range(len(prev) + 1):
                res.append(prev[:i] + [curr] + prev[i:])

        print(res)
        return res

        
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        curr_sums = {0 : 1}

        for num in nums:
            new_sums = defaultdict(int)
            for curr_sum in curr_sums.keys():
                new_sums[curr_sum + num] += curr_sums[curr_sum]
                new_sums[curr_sum - num] += curr_sums[curr_sum]
            curr_sums = new_sums

        return curr_sums[target]
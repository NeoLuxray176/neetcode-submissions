class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False

        curr_sums = {0 : 1}
        target = sum(nums) // 2

        for num in nums:
            new_sums = defaultdict(int)
            for curr_sum in curr_sums.keys():
                if curr_sum + num == target:
                    return True

                new_sums[curr_sum] += curr_sums[curr_sum]
                new_sums[curr_sum + num] += curr_sums[curr_sum]
            
            curr_sums = new_sums

        return False

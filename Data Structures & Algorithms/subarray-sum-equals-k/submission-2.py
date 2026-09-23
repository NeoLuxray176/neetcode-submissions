class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = curr_sum = 0
        prefix_sums = { 0 : 1}

        # The equation we are after is curr_sum_i_to_j = (curr_sum_j - curr_sum_i) = k
        # Rearrange to curr_sum_j = k = curr_sum_i

        for num in nums:
            curr_sum += num
            diff = curr_sum - k

            res += prefix_sums.get(diff, 0)
            prefix_sums[curr_sum] = 1 + prefix_sums.get(curr_sum, 0)

        return res


        


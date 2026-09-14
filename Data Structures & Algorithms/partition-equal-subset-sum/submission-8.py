class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)

        if n % 2 != 0:
            return False

        target = n // 2

        dps = set()
        dps.add(0)

        for num in nums:
            next_dps = set()
            for dp in dps:
                if target == dp + num:
                    return True

                next_dps.add(dp)
                next_dps.add(dp + num)

            dps = next_dps

        return target in dps
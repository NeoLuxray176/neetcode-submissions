class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)

        su = sum(nums)

        if su % 2 != 0:
            return False

        target = su // 2

        dp = set()
        dp.add(0)

        for num in nums:
            nextdp = set()
            for d in dp:
                if target == d + num:
                    return True
                # if target < d + num:
                    # continue

                nextdp.add(d)
                nextdp.add(d + num)
            dp = nextdp

        return target in dp
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right

        while left <= right:
            middle = (left + right) // 2

            duration = 0
            for pile in piles:
                duration += math.ceil(pile / middle)

            if duration < h:
                res = middle
                right = middle - 1
            else:
                left = middle + 1

            # if duration > h:
            #     left = middle + 1
            # else:
            #     res = middle
            #     right = middle - 1

        return res

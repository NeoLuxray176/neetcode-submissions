class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = max(piles)

        while left <= right:
            middle = (left + right) // 2

            dur = 0
            for pile in piles:
                dur += math.ceil(pile / middle)
            
            if dur > h:
                left = middle + 1
            else:
                res = min(res, middle)
                right = middle - 1

        return res
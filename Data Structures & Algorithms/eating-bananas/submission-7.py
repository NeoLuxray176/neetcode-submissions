class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_val = 1
        max_val = max(piles)
        old_duration = -1
        res = max_val

        while min_val <= max_val:
            middle = (min_val + max_val) // 2

            duration = 0
            for pile in piles:
                time_to_eat = math.ceil(pile / middle)
                duration += time_to_eat
            
            if duration > h:
                min_val = middle + 1
            elif duration <= h:
                res = middle
                max_val = middle - 1
            
        return res



        

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:   
        if not triplets:
            return False

        a = b = c = float("-inf")

        for d, e, f in triplets:
            if max(a, d) <= target[0] and max(b, e) <= target[1] and max(c, f) <= target[2]:
                a, b, c = max(a, d), max(b, e), max(c, f)

        if [a, b, c] == target:
            return True
        else:
            return False

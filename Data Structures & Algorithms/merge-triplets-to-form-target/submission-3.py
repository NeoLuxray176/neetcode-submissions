class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        curr = [0, 0, 0]

        for a, b, c in triplets:
            if a <= target[0] and b <= target[1] and c <= target[2]:
                curr[0] = max(curr[0], a)
                curr[1] = max(curr[1], b)
                curr[2] = max(curr[2], c)

        if curr[0] == target[0] and curr[1] == target[1] and curr[2] == target[2]:
            return True

        return False


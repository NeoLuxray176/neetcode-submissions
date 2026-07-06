class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # We can merge a triplet if it holds that one of the values is equal to the target values
        # and the two other values are smaller or equal to the target value

        a, b, c = False, False, False

        for triplet in triplets:
            if triplet[0] == target[0]:
                if triplet[1] <= target[1] and triplet[2] <= target[2]:
                    a = True
            if triplet[1] == target[1]:
                if triplet[0] <= target[0] and triplet[2] <= target[2]:
                    b = True
            if triplet[2] == target[2]:
                if triplet[0] <= target[0] and triplet[1] <= target[1]:
                    c = True

        return a and b and c
            
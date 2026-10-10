class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counts = Counter(hand)

        for card in sorted(counts):
            count = counts[card]
            if count == 0:
                continue

            for i in range(groupSize):
                if card + i in counts and counts[card + i] >= count:
                    counts[card + i] -= count
                else:
                    return False

        return True

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counts = Counter(hand)

        for card in sorted(counts):
            if counts[card] == 0:
                continue
            for i in range(groupSize):
                if card + i in counts and counts[card + i] > 0:
                    counts[card + i] -= 1
                else:
                    return False

        return True

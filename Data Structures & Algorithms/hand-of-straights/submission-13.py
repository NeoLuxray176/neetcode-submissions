class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counts = Counter(hand)

        for card in sorted(counts):
            count = counts[card]

            if counts[card] == 0:
                continue
            for i in range(card, card + groupSize):
                if counts[i] < count:
                    return False
                counts[i] -= count

        return True

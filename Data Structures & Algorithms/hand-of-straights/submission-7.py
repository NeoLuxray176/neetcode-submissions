class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counter = Counter(hand)

        for card in hand:
            count = counter[card]
            if count == 0:
                continue
            for i in range(card, card + groupSize):
                if count <= counter[i]:
                    counter[i] -= count
                else:
                    return False

        return True

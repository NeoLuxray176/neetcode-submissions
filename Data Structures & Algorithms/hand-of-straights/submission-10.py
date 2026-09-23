class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counter = Counter(hand)

        for card in sorted(hand):
            count = counter[card]
            if count == 0:
                continue
            
            for i in range(card, card + groupSize):
                if counter[i] < count:
                    return False
                counter[i] -= count

        return True
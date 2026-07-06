class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        # Counter is a subclass of dict
        # It allows easy tallies and counts
        count = Counter(hand)

        # The key idea is that we iterate through the list and then for each of the values
        # find the lowest possible start value.
        # This way we don't take away anything from sequences that start earlier.
        # (This is the key insight for this to work.)
        # (Further note that there may be gaps in the overall sequence.)
        #
        # Then we simply iterate from the lowest possible start to the end of the group
        # and decrement the counts.
        # If there is ever a number that isn't present, then we return false.
        # If we never return false the condition holds.

        for num in hand:
            start = num
            while count[start - 1]:
                start -= 1
            while count[start]:
                for i in range(start, start + groupSize):
                    if not count[i]:
                        return False
                    count[i] -= 1
            start += 1
        return True
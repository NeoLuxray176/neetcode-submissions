class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Task

        # Constraints

        # General Idea:
        # Remember the last occurance of any character, then on the next occurance we can compute the
        # longest substring between them

        # Idea:
        # 1. Store two variables best where we store the current result, second left which is the leftmost point
        # in the string where we haven't seen any repetition. Both are intitially zero. 
        # In a map store the last occurance for each character
        # 2. iterate over all characters, store the last occurance and compute the current best result.
        # 2.1 we can compute the current best result by storing the last occurance (or zero) in left and then
        # computing (right - left + 1) (+1 because the last occurance is not included in left) where right is the
        # index of the current character.
        # 3. we store the max of the new result and the previously best result in the current result variable.

        left = 0
        best = 0

        last_seen = {}

        for (right, character) in enumerate(s):
            if character in last_seen:
                left = last_seen[character]
            last_seen[character] = right + 1

            best = max(best, right - left + 1)

        return best
                
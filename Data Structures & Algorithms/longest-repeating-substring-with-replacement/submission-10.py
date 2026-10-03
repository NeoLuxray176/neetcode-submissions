class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Task:
        # Constraints:
        # General Idea:
        # Two pointers
        # Keep track of the number of occurances of each character between these two pointers.
        # As long as the character that occurs the most, occurs not more than ((right - left) - k) times
        # we can compensate for that and increase right. Otherwise we increase left and make our window smaller.
        # Use a variable to keep track of the best result we have seen so far.

        # Idea:
        # 1. two pointers left, right pointing both to the first character
        # 2. a map storing the occurances of each of the characters seen so far
        # 3. iterate over all characters and corresponding right positions and increment the number of occurances
        # 4. we violate the condition ((right - left) - max_occurance) > k, decrement the left pointer until we
        # the condition holds or left == right
        # 5. compute the current window and store in the current res variable
        # 6. return the variable

        left, best = 0, 0
        counts = [0] * 26
        max_freq = 0

        for right, character in enumerate(s):
            counts[ord(character) - ord('A')] += 1
            max_freq = max(max_freq, counts[ord(character) - ord('A')])
            if left <= right and (right - left + 1) - max_freq > k:
                counts[ord(s[left]) - ord('A')] -= 1
                left += 1

            best = max(best, (right - left + 1))

        return best

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # General Idea
        # We keep track of the occurances of each character
        # For each new character we count how many times it occurs.
        # We need to replace more than k characters if there are more than k characters in 
        # the substring that are different from the character that occurs the most times.
        # We can compute this by taking the length of the current substring which is given by
        # right - left + 1 and then subtracting the times the character that occurs the most often
        # occurs. If this is larger than k we need to shrink from the left.
        count = {}
        res = 0

        left = 0
        maxF = 0

        for right, char in enumerate(s):
            count[char] = 1 + count.get(char, 0)
            maxF = max(maxF, count[char])

            while (right - left + 1) - maxF > k:
                count[s[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)

        return res
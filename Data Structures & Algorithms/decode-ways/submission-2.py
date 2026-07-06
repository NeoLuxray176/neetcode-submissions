class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        # Use a list instead of a dict. 
        # Size is n + 1 to accommodate the base case at the end.
        dp = [0] * (n + 1)
        
        # Base case: An empty string at the end has 1 way to be decoded
        dp[n] = 1

        for i in range(n - 1, -1, -1):
            # Case 1: Leading zero
            if s[i] == "0":
                dp[i] = 0
                continue # Skip to next iteration, no further processing needed for '0'

            # Case 2: Single digit decoding
            # If it's not '0', we can always decode it as a single digit
            # So it inherits the number of ways from the next position
            dp[i] = dp[i + 1]

            # Case 3: Two digit decoding
            # Check boundaries and if the two digits form a valid number (10-26)
            # So we can decode in the number of ways from the position two numbers away
            if i < n - 1:
                if s[i] == "1" or (s[i] == "2" and s[i + 1] <= "6"):
                    dp[i] += dp[i + 2]

        return dp[0]
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s) : 1}

        for i in range(len(s) - 1, -1, -1):
            print(f"i={i}")
            if s[i] == "0":
                # If there is a zero we cannot decode this
                dp[i] = 0
            else:
                # If there isn't a zero we can decode in the same amount
                # of ways as the number before
                dp[i] = dp[i + 1]
            
            if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"):
                dp[i] += dp[i + 2]


        print(dp)
        return dp[0]
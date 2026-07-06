class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)

        dp = [False] * (n + 1)
        dp[n] = True

        for i in range(n -1, -1 , -1):
            for word in wordDict:
                m = len(word)

                if i + m <= n:
                    print(f"Comparing {s[i:i+m]} and {word}")
                    if s[i:i+m] == word:
                        if dp[i+m] == True:
                            dp[i] = True
        
        return dp[0]
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(n + 1):
            for word in wordDict:
                # print(f"Checking {s[i:]} for {word} {dp[i] and s[i:].startswith(word)} {i + len(word)} {n}")
                if dp[i] and s[i:].startswith(word) and i + len(word) <= n:
                    dp[i + len(word)] = True

        # print(dp)
        return dp[-1]
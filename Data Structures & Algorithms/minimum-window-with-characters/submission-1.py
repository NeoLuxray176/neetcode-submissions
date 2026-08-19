class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res, l = None, 0
        cnt, window = Counter(t), Counter()
        
        for h in range(len(s)):
            window[s[h]] += 1
            
            if window >= cnt:
                while window[s[l]] > cnt[s[l]]:
                    window[s[l]] -= 1
                    l += 1

                if not res or (h - l + 1) < len(res):
                    res = s[l:h + 1]
        return res if res else ""
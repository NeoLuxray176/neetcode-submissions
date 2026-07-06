class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        big_dict = defaultdict(list)
        n = len(strs)

        for i in range(n):
            char_freqs = [0] * 26
            for c in strs[i]:
                char_freqs[ord(c) - ord("a")] += 1
            
            big_dict[tuple(char_freqs)].append(strs[i])

        return list(big_dict.values())
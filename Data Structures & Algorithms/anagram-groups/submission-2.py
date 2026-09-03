class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}

        for word in strs:
            word_sorted = list(word)
            word_sorted.sort()
            word_sorted = "".join(word_sorted)
            # print(f"Checking {word_sorted}")
            if word_sorted in dictionary:
                dictionary[word_sorted].append(word)
            else:
                dictionary[word_sorted] = [word]

        res = []
        for words in dictionary.values():
            res.append(words)

        # print(res)
        return res

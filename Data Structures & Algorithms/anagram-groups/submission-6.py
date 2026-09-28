class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}

        for string in strs:
            curr = "".join(sorted(string))
            if curr in dictionary:
                dictionary[curr].append(string)
            else:
                dictionary[curr] = [string]

        return list(dictionary.values())
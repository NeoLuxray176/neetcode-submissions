class Solution:
    def romanToInt(self, s: str) -> int:
        dictionary = {
            "M" : 1000,
            "D" : 500,
            "C" : 100,
            "L" : 50,
            "X" : 10, 
            "V" : 5,
            "I" : 1,
        }

        res = 0
        i = 0
        while i < len(s):
            if i < len(s) - 1 and dictionary[s[i]] < dictionary[s[i + 1]]:
                res += (dictionary[s[i + 1]] - dictionary[s[i]])
                i += 2
            else:
                res += dictionary[s[i]]
                i += 1

        return res

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # word="apple"
        # abbr="a4"
        # expect true

        i = 0
        curr_digit = ""
        while i < len(abbr):
            # print(abbr[i], abbr[i].isdigit())
            if abbr[i].isdigit():
                if abbr[i] == "0":
                    return False
                curr_digit += abbr[i]
                i += 1
            elif curr_digit:
                i += int(curr_digit)
                curr_digit = ""
            else:
                if word[i] != abbr[i]:
                    return False
                i += 1
        
        if curr_digit:
            return i + int(curr_digit) - 1 == len(word)

        # print(i, len(word))
        return i == len(word)
                

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        mapping = {
            "1" : [],
            "2" : ["a", "b", "c"],
            "3" : ["d", "e", "f"],
            "4" : ["g", "h", "i"],
            "5" : ["j", "k", "l"],
            "6" : ["m", "n", "o"],
            "7" : ["p", "q", "r", "s"],
            "8" : ["t", "u", "v"],
            "9" : ["w", "x", "y", "z"]
        }

        res = []

        def backtrack(path : List[str], index : int):
            if index >= len(digits):
                res.append("".join(path))
                return

            for num in mapping[digits[index]]:
                path.append(num)
                backtrack(path, index + 1)
                path.pop()

        backtrack([], 0)

        return res
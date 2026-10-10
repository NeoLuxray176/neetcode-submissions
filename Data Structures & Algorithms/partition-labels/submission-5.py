class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurance = {}

        for i, character in enumerate(s):
            last_occurance[character] = i

        res = []
        curr, length = -1, 1
        

        for i, character in enumerate(s):
            curr = max(curr, last_occurance[character])

            if i == curr:
                res.append(length)
                length = 0
            length += 1

        return res

            
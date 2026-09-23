class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurance = {}
        res = []

        for i, character in enumerate(s):
            last_occurance[character] = i
        
        end = 0
        anchor = 0
        for i, character in enumerate(s):
            end = max(end, last_occurance[character])

            if i == end:
                res.append(end + 1 - anchor)
                anchor = i + 1

        return res


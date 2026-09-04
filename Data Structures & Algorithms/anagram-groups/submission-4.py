class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        diction = {}

        for st in strs:
            curr = "".join(sorted(st))
            # print(curr)
            if curr in diction:
                diction[curr].append(st)
            else:
                diction[curr] = [st]

        return list(diction.values())
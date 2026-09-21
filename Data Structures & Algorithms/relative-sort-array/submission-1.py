class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        hmap = {}
        for i in range(len(arr1)):
            if arr1[i] in hmap:
                hmap[arr1[i]].append(i)
            else:
                hmap[arr1[i]] = [i]
        res = []

        for i, val in enumerate(arr2):
            for _ in range(len(hmap.get(val, 0))):
                res.append(val)
            hmap.pop(val)

        for val in sorted(hmap.keys()):
            for _ in range(len(hmap.get(val, 0))):
                res.append(val)
            

        return res


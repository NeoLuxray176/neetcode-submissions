class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = [-1]
        last = arr[-1]

        for i in range(n - 1 - 1, -1, -1):
            tmp = last
            last = max(last, arr[i])
            res.append(tmp)

        return list(reversed(res))


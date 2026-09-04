class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        diction = {}

        for num in nums:
            if not num in diction:
                diction[num] = 1
            else:
                diction[num] = diction[num] +  1

        arr = list(diction.items()) # tuples of (key, value)
        arr.sort(key=lambda x: -x[1])

        res = []
        for i in range(k):
            res.append(arr[i][0])

        return res

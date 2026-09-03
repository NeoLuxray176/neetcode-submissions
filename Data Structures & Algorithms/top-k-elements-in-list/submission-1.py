class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cntr = {}

        for num in nums:
            if num in cntr:
                cntr[num] += 1
            else:
                cntr[num] = 1
            # print(f"{cntr}")

        interm = []
        for key, val in cntr.items():
            # print(f"{key} {val}")
            interm.append((key, val))

        # print(interm)
        interm.sort(key = lambda x: -x[1])
        # print(interm)

        res = []

        for i in range(k):
            res.append(interm[i][0])

        return res
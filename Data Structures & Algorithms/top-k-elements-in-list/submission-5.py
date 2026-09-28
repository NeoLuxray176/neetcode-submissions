class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for key, value in count.items():
            buckets[value].append(key)

        res = []
        
        for bucket in reversed(buckets):
            for key in bucket:
                res.append(key)
                if len(res) == k:
                    return res

        return res
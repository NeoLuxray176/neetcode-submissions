class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        diccy = {}

        for i, num in enumerate(nums2):
            diccy[num] = i

        m = max(nums2)
        res = []
        for num in nums1:
            idx = diccy[num]
            while idx < len(nums2):
                if nums2[idx] > num:
                    break
                idx += 1
            if idx == len(nums2):
                res.append(-1)
            else:
                res.append(nums2[idx])

        return res
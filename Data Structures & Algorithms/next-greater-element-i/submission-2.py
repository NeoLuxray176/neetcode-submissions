class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)

        for i in range(len(nums1)):
            found_equal = False
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    found_equal = True
                if found_equal and nums1[i] < nums2[j]:
                    res[i] = nums2[j]
                    break

        return res




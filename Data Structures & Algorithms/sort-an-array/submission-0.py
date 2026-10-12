class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        if n == 1:
            return nums
        if n == 2:
            if nums[0] < nums[1]:
                return nums
            else:
                return [nums[1], nums[0]]

        half = n // 2
        a, b = self.sortArray(nums[:half]), self.sortArray(nums[half:])

        i = j = 0
        res = []

        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                res.append(a[i])
                i += 1
            else:
                res.append(b[j])
                j += 1
        while i < len(a):
            res.append(a[i])
            i += 1
        while j < len(b):
            res.append(b[j])
            j += 1

        return res



        
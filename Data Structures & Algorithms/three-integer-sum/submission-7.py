class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()

        res = []
        
        for i in range(n):
            if nums[i] > 0:
                continue

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1

            while left < right:
                a, b, c = nums[i], nums[left], nums[right]
                if a + b + c == 0:
                    res.append([a, b, c])
                    left += 1
                    right -= 1
                    while nums[left - 1] == nums[left] and left < right:
                        left += 1
                if a + b + c < 0:
                    left += 1
                if a + b + c > 0:
                    right -= 1

        return res
            
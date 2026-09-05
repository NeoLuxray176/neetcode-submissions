class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()

        res = []

        for i in range(n):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1
            while left < right:
                a, b, c = nums[i], nums[left], nums[right]
                curr_sum = a + b + c
                if curr_sum > 0:
                    right -= 1
                if curr_sum < 0:
                    left += 1
                if curr_sum == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    right -= 1
                    left += 1

                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return res
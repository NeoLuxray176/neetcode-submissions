class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)

        last_negative = 0
        while last_negative < n and nums[last_negative] < 0:
            last_negative += 1
        
        for i in range(n):
            nums[i] = nums[i] * nums[i]

        left = last_negative - 1
        right = last_negative
        res = []

        while left >= 0 and right < n:
            # print(nums[left], nums[right])
            if nums[left] < nums[right]:
                res.append(nums[left])
                left -= 1
            else:
                res.append(nums[right])
                right += 1

        while left >= 0:
            res.append(nums[left])
            left -= 1
        
        while right < n:
            res.append(nums[right])
            right += 1

        return res

        


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        
        arr = [0] * n
        arr[0], arr[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, n):
            # Do not rob this house but rob the previous house
            # Rob this house but then we can't rob the previous house            
            arr[i] = max(arr[i - 1], arr[i - 2] + nums[i])

        return arr[-1]
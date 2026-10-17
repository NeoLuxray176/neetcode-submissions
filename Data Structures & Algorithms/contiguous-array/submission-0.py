class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                nums[i] = -1

        mp = {0 : -1}
        res = curr = 0
        
        for i in range(n):
            curr += nums[i]
            if curr not in mp:
                mp[curr] = i
            else:
                res = max(res, i - mp[curr])
            
        return res
class Solution:
    def climbStairs(self, n: int) -> int:
        # 0 1 2 3 4
        # 0 1 2 3 5

        if n <= 1:
            return 1
        if n <= 2:
            return 2
        
        arr = [0] * (n+1)
        arr[0] = 1
        arr[1] = 2
        

        for i in range(2, n+1):
            arr[i] = arr[i-1] + arr[i-2]
        

        return arr[n-1]
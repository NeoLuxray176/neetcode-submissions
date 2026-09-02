class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_arr = list(s)
        t_arr = list(t)
        s_arr.sort()
        t_arr.sort()

        # print(s_arr)

        for i in range(len(s_arr)):
            # print(f"Checking {s_arr[i]} and {t_arr[i]}")
            if s_arr[i] != t_arr[i]:
                return False

        return True
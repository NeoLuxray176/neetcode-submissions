class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        for i in range(n // 2):
            # print(s)
            # print(s[i], s[n - 1 - i])
            tmp = s[i]
            s[i] = s[n - 1 - i]
            s[n - 1 - i] = tmp
            # print(s[i], s[n - 1 - i])
            # print(s)
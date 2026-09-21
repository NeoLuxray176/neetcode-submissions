class Solution:
    def isUgly(self, n: int) -> bool:
        spf = [0] * (n + 1)
        spf[1] = 1

        for i in range(2, n + 1):
            spf[i] = i

        for i in range(4, n + 1, 2):
            spf[i] = 2

        for i in range(3, int(n ** 0.5) + 1, 2):
            if spf[i] == i:
                for j in range(i * i, n + 1, i):
                    if spf[j] == j:
                        spf[j] = i

        res = []

        while n != 1:
            a = spf[n]
            res.append(a)
            n = n // a

        for re in res:
            if re != 2 and re != 3 and re != 5:
                return False
        return True
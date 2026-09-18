class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        res = 0
        for i in range(n):
            types = set()
            j = i
            while j < n and (len(types) < 2 or fruits[j] in types):
                types.add(fruits[j])
                j += 1
            res = max(res, j - i)
        return res
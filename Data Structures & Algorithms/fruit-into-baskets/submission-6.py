class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # Instead of restarting from each position, we maintain a sliding window that always contains at most two fruit types. 
        # When we encounter a third type, we shrink the window from the left until only two types remain.

        # A hash map tracks the count of each fruit type in the current window. When a count drops to zero, we remove that type from the map.
 
        count = defaultdict(int)
        l, total, res = 0, 0, 0

        for r in range(len(fruits)):
            count[fruits[r]] += 1
            total += 1

            while len(count) > 2:
                f = fruits[l]
                count[f] -= 1
                total -= 1
                l += 1
                if not count[f]:
                    count.pop(f)

            res = max(res, total)

        return res
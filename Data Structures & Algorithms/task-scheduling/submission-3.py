class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        counts = [0] * 26
        for task in tasks:
            counts[ord(task) - ord("A")] += 1

        counts.sort()
        maxIdle = counts[-1]
        idleTime = (maxIdle - 1) * n


        for i in range(25):
            # print(f"{idleTime} min({maxIdle - 1}, {counts[i]}))")
            idleTime -= min(maxIdle - 1, counts[i])

        # print(f"{idleTime}")
        return max(0, idleTime) + len(tasks)
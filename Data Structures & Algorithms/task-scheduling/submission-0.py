class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Each task takes one time unit but between executions of the same kind of task we need
        # n time units of downtime
        # So we need at least idle time for the task that occurs the most

        # Note that the task that occurs the second most often can already slot in easily between the occurances of the most occuring task, so we do not need to consider it.

        # We only need to consider the leftover idle time

        counts = [0] * 26

        for task in tasks:
            counts[ord(task) - ord("A")] += 1

        counts.sort()
        maxIdle = counts[25]
        idle = (maxIdle - 1) * n

        

        for i in range(24, -1, -1):
            idle -= min(maxIdle - 1, counts[i])

        return max(0, idle) + len(tasks)
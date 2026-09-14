class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # We can either finish all tasks without waiting
        # for example if all tasks are distinct
        # Or we can try to slot in the other tasks in the waiting times


        occurances = [0] * 26

        for task in tasks:
            occurances[ord(task) - ord('A')] += 1

        occurances.sort()

        maxIdle = occurances[-1]
        idle_time = (maxIdle - 1) * n
        
        for i in range(25):
            idle_time -= min(maxIdle - 1, occurances[i])

        return len(tasks) + max(0, idle_time)


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)

        maximum = max(counter.values())
        ties = len([key for key in counter if counter[key] == maximum])

        return max(len(tasks), (n + 1) * (maximum - 1) + ties)
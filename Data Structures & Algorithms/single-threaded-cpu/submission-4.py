class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # Task
        # Given a list of tasks give the execution order of those tasks
        # A task can be started at time enqueueTime and takes processingTime time units
        # If two tasks can be started at the same time the shorter task will be chosen
        # Tasks cannot be interrupted

        # Constraints
        # The tasks are not sorted

        # General Idea
        # Sort tasks by enqueueTime and then by duration
        # Simulate the execution with a timer that ticks forward.
        # We don't even need enqueue time apart from it telling us the order of the execution, we don't need to show bubbles
        # in the pipeline.

        # So we sort the tasks and then add them to our output array. 
        # There is one issue, we will lose the index, so we we have to transform the list of tasks first.
        # Switching to a minheap does not help us. We still need to sort the full array

        arr = []
        for i, task in enumerate(tasks):
            arr.append((task[0], task[1], i))

        arr.sort()

        res = []

        i = 0
        curr_time = arr[0][0]
        heap = []
        heapq.heapify(heap)

        while i < len(tasks) or heap:
            while i < len(tasks) and arr[i][0] <= curr_time:
                heapq.heappush(heap, (arr[i][1], arr[i][2]))
                i += 1

            if heap:
                processing_time, idx = heapq.heappop(heap)
                res.append(idx)
                curr_time += processing_time
            else:
                curr_time = arr[i][0]

        return res
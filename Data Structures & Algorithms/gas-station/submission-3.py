class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # General Idea
        #  Since we can choose the starting point, we can complete the circuit as long as the remaining gas after one round is positive
        if sum(gas) < sum(cost):
            return -1

        start_idx = 0
        tank = total = 0

        for i in range(len(gas)):
            balance = gas[i] - cost[i]

            total += balance
            tank += balance

            if tank < 0:
                start_idx = i + 1
                tank = 0

        # return start_idx if total >= 0 else -1
        return start_idx

        # total = tank = start = 0
        # for i, (fuel, expense) in enumerate(zip(gas, cost)):
        #     balance = fuel - expense
        #     total += balance
        #     tank += balance
        #     if tank < 0:
        #         start = i + 1
        #         tank = 0
        # return start if total >= 0 else -1
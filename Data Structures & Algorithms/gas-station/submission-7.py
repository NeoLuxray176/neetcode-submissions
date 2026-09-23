class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        start = 0
        tank = total = 0

        for i, (incoming, outgoing) in enumerate(zip(gas, cost)):
            balance = incoming - outgoing
            tank += balance
            total += balance

            if tank < 0:
                start = i + 1
                tank = 0

        return start if total >= 0 else -1
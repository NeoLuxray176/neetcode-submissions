class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # We can complete the circle if there is enough gas to go around
        # We find the start point by setting the start point to the last point
        # where we ran out of gas

        start = 0
        curr = 0
        total = 0

        for i, (new_gas, new_cost) in enumerate(zip(gas, cost)):
            curr += (new_gas - new_cost)
            total += (new_gas - new_cost)

            # print(i, new_gas, new_cost, curr)

            if curr < 0:
                start = i + 1
                curr = 0

        if total < 0:
            return -1

        return start
from typing import Dict, List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Adjacency list: airport -> airports reachable by a still-unused ticket.
        # Only airports that appear as an origin get a key.
        destinations_from: Dict[str, List[str]] = {origin: [] for origin, _ in tickets}

        # Sorting the tickets first means each destination list is built in
        # lexical order, so the DFS naturally tries the smallest code first.
        tickets.sort()
        for origin, destination in tickets:
            destinations_from[origin].append(destination)

        # This list is both the DFS path and the final answer.
        itinerary: List[str] = ["JFK"]
        # n tickets are consumed by a route through n + 1 airports.
        route_length = len(tickets) + 1

        def visit(airport: str) -> bool:
            # Success: every ticket has been used exactly once.
            if len(itinerary) == route_length:
                return True
            # Dead end: no ticket was ever issued out of this airport.
            if airport not in destinations_from:
                return False

            # Snapshot, because destinations_from[airport] is mutated in the loop.
            candidates = list(destinations_from[airport])
            for index, next_airport in enumerate(candidates):
                # "Use" the ticket by removing it from the adjacency list.
                destinations_from[airport].pop(index)
                itinerary.append(next_airport)

                if visit(next_airport):
                    return True

                # Backtrack: return the ticket and undo the step.
                destinations_from[airport].insert(index, next_airport)
                itinerary.pop()

            return False

        visit("JFK")
        return itinerary
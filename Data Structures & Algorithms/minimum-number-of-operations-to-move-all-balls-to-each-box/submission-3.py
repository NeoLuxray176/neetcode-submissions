class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # Task
        # Given a list of boxes of length n.
        # Calculate the number of operations we have to do to move all balls to the i-th box. For all i in [0,n].
        # An operation constitutes the move of one ball to an adjacent box.
        # So moving two balls into an adjacent box takes two operations.
        # Moving one ball into an adjacent box takes two operations. Moving it two boxes takes two operations.

        # Constraints:
        # We may have zero boxes, in that case it takes no operations
        
        # General idea:
        # Brute force approach:
        # For each index, calculate the result explicitly by computing the distance of every other ball to our box.
        # So when calculating the operations for index 5, a ball at index 2. Would have to be moved to index 3, 4, and 5. Which
        # is 5 - 2 = 3 operations.
        # For every index we have to compute the operations required for all other indices. This is n * (n-1) so in O(n^2)

        # Can we do better?
        # Given a prefix operations count and a suffix operations count we can compute the number of operations as
        # 2 * (poc[i - 1] + soc[i + 1]).
        # Now easier we could just combine poc[i] and soc[i] because at that point the number of operations to move all balls to the left of
        # us is stored at poc[i].
        # In addition we need the combined number of balls in the next and previous box instead of simply the number of original balls. I only discovered this during the implementation.

        # Can we do even better?
        # No, because we do need information about the whole left and right side.
        # So this would run in linear time and uses linear space as well.

        # Tests
        # "110"
        # [1, 1, 3]

        boxes = list(boxes) # "110" -> ["1", "1", "0"]
        n = len(boxes) # 3
        for i in range(n): # [1, 1, 0]
            boxes[i] = int(boxes[i])

        prefix_oc = [0] * n
        suffix_oc = [0] * n

        prefix_sum = 0
        for i in range(1, n):
            prefix_sum += boxes[i - 1]
            prefix_oc[i] = prefix_oc[i - 1] + prefix_sum
            # [0, 0, 0]
            # i = 1; [0, 1, 0]
            # i = 2; [0, 1, 3]
        # print("prefix_oc", prefix_oc)

        suffix_sum = 0
        for i in range((n - 1) - 1, -1, -1):
            suffix_sum += boxes[i + 1]
            suffix_oc[i] = suffix_oc[i + 1] + suffix_sum
            # [0, 0, 0]
            # i = 1; [0, 0, 0]
            # i = 1; [1, 0, 0]
        # print("suffix_oc", suffix_oc)

        res = [0] * n
        for i in range(n):
            res[i] = prefix_oc[i] + suffix_oc[i]

        return res

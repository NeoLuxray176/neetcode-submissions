class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # We want to look at the middle value if it is larger than target
        # go to the left half; if it is smaller than the target value go to the right half
        # and look at the middle point for each of the halves.
        # This will half our search space in each iteration giving us logarithmic runtime

        middle = len(nums) // 2
        tries = 0

        print(f"Looking at {middle} and value {nums[middle]}")

        while nums[middle] != target and tries < len(nums) + 1:
            print(f"Run while")
            new_middle = middle
            if nums[middle] < target:
                new_middle = middle + middle // 2
            else:
                new_middle = middle // 2
            if new_middle == middle:
                break
            print(f"Moving from {middle} to {new_middle}")
            middle = new_middle
            tries += 1


        return middle if nums[middle] == target else -1
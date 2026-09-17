class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = list(reversed(sorted(nums)))

        # print(nums)

        curr = nums[0]

        # for i, num in enumerate(nums):
        for i in range(len(nums)):
            # print(f"{curr} {nums[i]} {k}")
            # if curr != nums[i]:
                # curr = nums[i]
                # k -= 1

            if k == 0:
                # print(f"{curr} {nums[i]} {k}")
                return curr
            curr = nums[i]
            k -= 1


        return curr









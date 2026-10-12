class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        temp = [0] * n

        def merge_sort(left: int, right: int) -> None:
            # Sort nums[left:right], where right is exclusive.
            if right - left <= 1:
                return

            mid = (left + right) // 2

            merge_sort(left, mid)
            merge_sort(mid, right)

            # Already sorted; avoid unnecessary merging.
            if nums[mid - 1] <= nums[mid]:
                return

            i, j, k = left, mid, left

            # Merge the two sorted halves into temp.
            while i < mid and j < right:
                if nums[i] <= nums[j]:
                    temp[k] = nums[i]
                    i += 1
                else:
                    temp[k] = nums[j]
                    j += 1
                k += 1

            while i < mid:
                temp[k] = nums[i]
                i += 1
                k += 1

            while j < right:
                temp[k] = nums[j]
                j += 1
                k += 1

            # Copy the merged range back into nums.
            for k in range(left, right):
                nums[k] = temp[k]

        merge_sort(0, n)
        return nums
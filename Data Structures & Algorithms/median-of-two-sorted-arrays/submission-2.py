class Solution:
    def findMedianSortedArrays(
        self,
        nums1: List[int],
        nums2: List[int],
    ) -> float:
        # Always binary-search the shorter array.
        # This gives O(log(min(m, n))) time and also keeps the partition
        # in the longer array valid.
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)

        # We want the left half to contain half of all elements.
        #
        # The +1 makes the left half contain the extra element when the
        # total number of elements is odd.
        half = (m + n + 1) // 2

        # i represents how many elements from nums1 go into the left half.
        #
        # We can choose anywhere from:
        #   0 elements from nums1
        # to
        #   all m elements from nums1
        lo, hi = 0, m

        while lo <= hi:
            # Partition nums1 after i elements.
            i = (lo + hi) // 2

            # Since the total left half must contain `half` elements,
            # nums2 must contribute the remaining elements.
            j = half - i

            # Values immediately around the two partitions:
            #
            # nums1: ... a_left | a_right ...
            # nums2: ... b_left | b_right ...
            #
            # +/- infinity handles partitions at the beginning or end
            # without special-case logic.
            a_left = nums1[i - 1] if i > 0 else float("-inf")
            a_right = nums1[i] if i < m else float("inf")

            b_left = nums2[j - 1] if j > 0 else float("-inf")
            b_right = nums2[j] if j < n else float("inf")

            # We found the correct partition when every value on the left
            # is <= every value on the right.
            #
            # Since both arrays are individually sorted, it is sufficient
            # to check only the values touching the partitions.
            if a_left <= b_right and b_left <= a_right:
                # Odd number of total elements:
                #
                # The left half contains one extra element, so the median
                # is the largest value on the left side.
                if (m + n) % 2 == 1:
                    return float(max(a_left, b_left))

                # Even number of total elements:
                #
                # Median is the average of:
                #   - largest value on the left
                #   - smallest value on the right
                return (
                    max(a_left, b_left)
                    + min(a_right, b_right)
                ) / 2

            # a_left is too large to belong on the left side.
            #
            # We took too many elements from nums1, so move its partition
            # to the left.
            if a_left > b_right:
                hi = i - 1

            # Otherwise b_left > a_right.
            #
            # We took too few elements from nums1, so move its partition
            # to the right.
            else:
                lo = i + 1
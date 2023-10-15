class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        https://leetcode.com/problems/merge-sorted-array/
        TC: O(m + n), SC: O(1) where m and n are given in the input
        """
        i = m - 1
        j = n - 1
        index_to_write = m + n - 1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[index_to_write] = nums1[i]
                i -= 1
            else:
                nums1[index_to_write] = nums2[j]
                j -= 1

            index_to_write -= 1

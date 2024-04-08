class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        """
        TC:O(m + n), SC:O(m + n) where m = len(nums1), n = len(nums2)
        """
        answer = []
        distinct1 = set(nums1)
        distinct2 = set(nums2)

        def find_distinct(a, b):
            not_in_b = []

            for num in a:
                if num not in b:
                    not_in_b.append(num)

            answer.append(not_in_b)

        find_distinct(distinct1, distinct2)
        find_distinct(distinct2, distinct1)

        return answer

class Solution:
    def validAnagram(self, s: str, t: str) -> bool:
        """
        https://leetcode.com/problems/contains-duplicate/description/
        TC: O(n) SC: O(n), n = len(s) or len(t)
        """
        if len(s) != len(t):
            return False

        def get_counts(s):
            counts = {}
            for char in s:
                if char not in counts:
                    counts[char] = 0
                counts[char] += 1
            return counts

        s_count = get_counts(s)
        t_count = get_counts(t)

        return s_count == t_count

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        TC: O(m + n), SC: O(1) where m = len(ransomNote) and n = len(magazine)
        """

        def get_counts(s):
            counts = [0] * 26
            for char in s:
                counts[ord(char) - ord("a")] += 1
            return counts

        note_counts = get_counts(ransomNote)
        mag_counts = get_counts(magazine)

        for char in ransomNote:
            index = ord(char) - ord("a")
            if mag_counts[index] < note_counts[index]:
                return False

        return True

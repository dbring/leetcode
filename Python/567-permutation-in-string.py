class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        TC: O(n), SC: O(1) where n = len(s2)
        """
        ALPHABET_SIZE = 26

        if len(s1) > len(s2):
            return False

        if s1 == s2:
            return True

        counts = [0] * ALPHABET_SIZE
        window = [0] * ALPHABET_SIZE
        for i in range(len(s1)):
            counts[ord(s1[i]) - ord("a")] += 1
            window[ord(s2[i]) - ord("a")] += 1

        matches = 0
        for i in range(ALPHABET_SIZE):
            if counts[i] == window[i]:
                matches += 1

        left = 0
        for right in range(len(s1), len(s2)):
            if matches == ALPHABET_SIZE:
                return True

            index = ord(s2[right]) - ord("a")
            window[index] += 1

            if window[index] == counts[index]:
                matches += 1
            elif window[index] == counts[index] + 1:
                matches -= 1

            index = ord(s2[left]) - ord("a")
            window[index] -= 1

            if window[index] == counts[index]:
                matches += 1
            elif window[index] == counts[index] - 1:
                matches -= 1

            left += 1

        return matches == ALPHABET_SIZE

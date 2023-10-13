from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """
        https://leetcode.com/problems/group-anagrams/description/
        TC: O(mn) SC: O(n) m = avg. len(strs[i]), n = len(strs)
        """
        anagram_groups = defaultdict(list)
        ALPHABET_SIZE = 26
        LOWERCASE_A = "a"

        for anagram in strs:
            char_counts = [0] * ALPHABET_SIZE

            for char in anagram:
                index = ord(char) - ord(LOWERCASE_A)
                char_counts[index] += 1

            counts = tuple(char_counts)
            anagram_groups[counts].append(anagram)

        return list(anagram_groups.values())

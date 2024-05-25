class Solution:
    def successfulPairs(
        self, spells: list[int], potions: list[int], success: int
    ) -> list[int]:
        """
        TC: O((n + m)logm), SC:O(m) where n = len(spells) and m = len(potions)
        """
        successes = []
        potions.sort()

        def binary_search_for_successes(spell):
            left = 0
            right = len(potions) - 1

            while left <= right:
                m = left + (right - left) // 2
                potion = potions[m]

                if spell * potion >= success:
                    right = m - 1
                else:
                    left = m + 1

            return len(potions) - left

        for spell in spells:
            successes.append(binary_search_for_successes(spell))

        return successes

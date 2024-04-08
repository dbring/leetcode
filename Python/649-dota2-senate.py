from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        """
        TC: O(n), SC:O(n) where n = len(senate)
        """
        n = len(senate)

        r_indices = deque([i for i in range(n) if senate[i] == "R"])
        d_indices = deque([i for i in range(n) if senate[i] == "D"])

        while r_indices and d_indices:
            r_idx = r_indices.popleft()
            d_idx = d_indices.popleft()

            if r_idx < d_idx:
                r_indices.append(r_idx + n)
            else:
                d_indices.append(d_idx + n)

        return "Radiant" if r_indices else "Dire"

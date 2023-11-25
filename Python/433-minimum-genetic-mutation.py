class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        """
        https://leetcode.com/problems/minimum-genetic-mutation/

        TC: O(n^2) SC:O(n) where n = len(bank)
        """
        from collections import deque

        queue = deque()

        if endGene not in bank:
            return -1

        queue.append((startGene, 0))
        visited = set()

        def get_valid_mutations(gene: str) -> list[str]:
            valid_mutations = []

            for mutation in bank:
                num_mutations = 0
                for c1, c2 in zip(mutation, gene):
                    if c1 != c2:
                        num_mutations += 1

                if num_mutations == 1:
                    valid_mutations.append(mutation)

            return valid_mutations

        while queue:
            gene, num_mutations = queue.popleft()

            if gene == endGene:
                return num_mutations

            if gene in visited:
                continue

            visited.add(gene)

            valid_mutations = get_valid_mutations(gene)

            for mutation in valid_mutations:
                queue.append((mutation, num_mutations + 1))

        return -1

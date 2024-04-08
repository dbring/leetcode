class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        """
        TC: O(n^2), SC: O(n^2) where n = len(grid)
        """
        n = len(grid)

        columns = [[] for _ in range(n)]

        for row in range(n):
            for col in range(n):
                columns[col].append(grid[row][col])

        equal = 0

        for row in range(n):
            for col in range(n):
                if grid[row] == columns[col]:
                    equal += 1

        return equal

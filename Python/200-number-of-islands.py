class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        """
        TC: O(mn), SC:O(mn), m = len(grid), n = len(grid[0])
        """
        num_rows = len(grid)
        num_cols = len(grid[0])
        LAND = "1"
        VISITED = "0"
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        number_of_islands = 0

        def is_land(row, col):
            return grid[row][col] == LAND

        def is_inbounds(row, col):
            return row >= 0 and row < num_rows and col >= 0 and col < num_cols

        def mark_island_visited(row, col):
            if not is_inbounds(row, col):
                return

            if not is_land(row, col):
                return

            grid[row][col] = VISITED

            for change_row, change_col in directions:
                new_row = row + change_row
                new_col = col + change_col
                mark_island_visited(new_row, new_col)

        for row in range(num_rows):
            for col in range(num_cols):
                if not is_land(row, col):
                    continue

                number_of_islands += 1
                mark_island_visited(row, col)

        return number_of_islands

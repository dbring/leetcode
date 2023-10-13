class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        """
        https://leetcode.com/problems/max-area-of-island/
        TC: O(mn), S:O(mn), m = len(grid), n = len(grid[0])
        """
        NUM_ROWS = len(grid)
        NUM_COLS = len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        LAND = 1
        VISITED = 0
        max_area_of_island = 0

        def is_inbounds(row, col):
            return row in range(NUM_ROWS) and col in range(NUM_COLS)

        def is_land(row, col):
            return grid[row][col] == LAND

        def find_island_area(row, col):
            if not is_inbounds(row, col):
                return 0

            if not is_land(row, col):
                return 0

            grid[row][col] = VISITED

            area = 1

            for change_row, change_col in directions:
                new_row = row + change_row
                new_col = col + change_col
                area += find_island_area(new_row, new_col)

            return area

        for row in range(NUM_ROWS):
            for col in range(NUM_COLS):
                if is_land(row, col):
                    area = find_island_area(row, col)
                    max_area_of_island = max(max_area_of_island, area)

        return max_area_of_island

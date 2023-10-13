class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        """
        https://leetcode.com/problems/pacific-atlantic-water-flow/
        TC: O(mn), SC: O(mn), m = len(heights), n = len(heights[0])
        """
        NUM_ROWS = len(heights)
        NUM_COLS = len(heights[0])
        directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        pacific = set()
        atlantic = set()
        result = []

        def is_inbounds(row, col):
            return row in range(NUM_ROWS) and col in range(NUM_COLS)

        def rain_can_flow(row, col, prev_height):
            return heights[row][col] >= prev_height

        def rain(row, col, ocean, prev_height):
            if not is_inbounds(row, col):
                return

            if not rain_can_flow(row, col, prev_height):
                return

            if (row, col) in ocean:
                return

            ocean.add((row, col))

            for change_row, change_col in directions:
                new_row = row + change_row
                new_col = col + change_col
                rain(new_row, new_col, ocean, heights[row][col])

        for col in range(NUM_COLS):
            rain(0, col, pacific, -1)
            rain(NUM_ROWS - 1, col, atlantic, -1)

        for row in range(NUM_ROWS):
            rain(row, 0, pacific, -1)
            rain(row, NUM_COLS - 1, atlantic, -1)

        for row in range(NUM_ROWS):
            for col in range(NUM_COLS):
                if (row, col) in pacific and (row, col) in atlantic:
                    result.append([row, col])

        return result

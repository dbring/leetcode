class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        https://leetcode.com/problems/surrounded-regions/
        TC: O(mn), SC: O(mn) m = len(board), n = len(board[0])
        Do not return anything, modify board in-place instead.
        """
        NUM_ROWS = len(board)
        NUM_COLS = len(board[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        CONNECTED_TO_EDGE = "#"

        def is_inbounds(row, col):
            return row in range(NUM_ROWS) and col in range(NUM_COLS)

        def is_visited(row, col):
            is_x = board[row][col] == "X"
            is_connected = board[row][col] == CONNECTED_TO_EDGE
            return is_x or is_connected

        def mark_connected_to_edge(row, col):
            if not is_inbounds(row, col):
                return

            if is_visited(row, col):
                return

            board[row][col] = CONNECTED_TO_EDGE

            for change_row, change_col in directions:
                new_row = row + change_row
                new_col = col + change_col
                mark_connected_to_edge(new_row, new_col)

        for col in range(NUM_COLS):
            mark_connected_to_edge(0, col)
            mark_connected_to_edge(NUM_ROWS - 1, col)

        for row in range(NUM_ROWS):
            mark_connected_to_edge(row, 0)
            mark_connected_to_edge(row, NUM_COLS - 1)

        for row in range(NUM_ROWS):
            for col in range(NUM_COLS):
                if board[row][col] == "O":
                    board[row][col] = "X"
                if board[row][col] == CONNECTED_TO_EDGE:
                    board[row][col] = "O"

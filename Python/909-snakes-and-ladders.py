from collections import deque


class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        n = len(board)
        queue = deque()

        def is_valid_position(position):
            return position <= n * n and position not in visited

        def is_snake_or_ladder(row, col):
            return board[row][col] != -1

        def get_row_and_col(position):
            row, col = divmod(position - 1, n)

            is_forward = row % 2 != 0

            if is_forward:
                return n - 1 - row, n - 1 - col
            else:
                return n - 1 - row, col

        INITIAL_POSITION = 1
        NUM_MOVES = 0
        queue.append((INITIAL_POSITION, NUM_MOVES))
        visited = set()

        while queue:
            position, num_moves = queue.popleft()

            row, col = get_row_and_col(position)

            if is_snake_or_ladder(row, col):
                position = board[row][col]

            if position == n * n:
                return num_moves

            for i in range(1, 7):
                new_position = position + i

                if is_valid_position(new_position):
                    visited.add(new_position)
                    queue.append((new_position, num_moves + 1))

        return -1

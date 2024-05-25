class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        from collections import deque

        NUM_ROWS = len(maze)
        NUM_COLS = len(maze[0])
        queue = deque()
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        WALL = "+"
        INITIAL_STEPS = 0
        visited = set()

        # Start at entrance
        queue.append((entrance[0], entrance[1], INITIAL_STEPS))

        def is_exit(row, col):
            return row == 0 or row == NUM_ROWS - 1 or col == 0 or col == NUM_COLS - 1

        def is_inbounds(row, col):
            return 0 <= row < NUM_ROWS and 0 <= col < NUM_COLS

        while queue:
            row, col, steps = queue.popleft()

            if (row, col) in visited or maze[row][col] == WALL:
                continue

            if is_exit(row, col) and [row, col] != entrance:
                return steps

            visited.add((row, col))

            for change_row, change_col in directions:
                new_row = row + change_row
                new_col = col + change_col

                if not is_inbounds(new_row, new_col):
                    continue

                queue.append((new_row, new_col, steps + 1))

        return -1

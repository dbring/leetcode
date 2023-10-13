from collections import deque


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        """
        TC: O(mn), SC: O(mn), m = len(grid), n = len(grid[0])
        """
        num_rows = len(grid)
        num_cols = len(grid[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        ROTTEN = 2
        FRESH = 1
        queue = deque()
        fresh_count = 0
        time = 0

        def is_rotten(row, col):
            return grid[row][col] == ROTTEN

        def is_fresh(row, col):
            return grid[row][col] == FRESH

        def is_inbounds(row, col):
            return row in range(num_rows) and col in range(num_cols)

        # Fill queue with rotten oranges
        for row in range(num_rows):
            for col in range(num_cols):
                if is_rotten(row, col):
                    queue.append((row, col))
                if is_fresh(row, col):
                    fresh_count += 1

        # BFS
        while queue:
            length = len(queue)

            for _ in range(length):
                row, col = queue.popleft()

                if is_fresh(row, col):
                    grid[row][col] = ROTTEN
                    fresh_count -= 1

                for change_row, change_col in directions:
                    new_row = row + change_row
                    new_col = col + change_col

                    if not is_inbounds(new_row, new_col):
                        continue

                    if not is_fresh(new_row, new_col):
                        continue

                    queue.append((new_row, new_col))

            if fresh_count:
                time += 1

        return time if fresh_count == 0 else -1

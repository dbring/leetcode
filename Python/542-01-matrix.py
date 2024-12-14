class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        TC: O(m * n), SC: O(m * n) where m = len(mat), n = len(mat[0])
        """
        from collections import deque

        queue = deque()
        DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        NUM_ROWS = len(mat)
        NUM_COLS = len(mat[0])

        def is_inbounds(row, col):
            return 0 <= row < NUM_ROWS and 0 <= col < NUM_COLS

        # Enqueue all (row, col, dist) pairs that are 0
        for row in range(NUM_ROWS):
            for col in range(NUM_COLS):
                if mat[row][col] == 0:
                    queue.append((row, col, 0))

        visited = set()

        while queue:
            row, col, dist = queue.popleft()

            if (row, col) in visited:
                continue

            if not is_inbounds(row, col):
                continue

            mat[row][col] = dist
            visited.add((row, col))

            for change_row, change_col in DIRECTIONS:
                new_row = row + change_row
                new_col = col + change_col
                queue.append((new_row, new_col, dist + 1))

        return mat

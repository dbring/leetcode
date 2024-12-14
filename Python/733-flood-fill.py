class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        """
        TC: O(m * n), SC: O(m * n) m = len(image), n = len(image[0])
        """
        DIRECTIONS = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        START_COLOR = image[sr][sc]

        def is_inbounds(row, col):
            return 0 <= row < len(image) and 0 <= col < len(image[0])

        visited = set()

        def fill(row, col):
            if not is_inbounds(row, col):
                return

            if (row, col) in visited:
                return

            if image[row][col] != START_COLOR:
                return

            image[row][col] = color
            visited.add((row, col))

            for change_row, change_col in DIRECTIONS:
                new_row = row + change_row
                new_col = col + change_col
                fill(new_row, new_col)

        fill(sr, sc)

        return image

    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        """
        BFS
        TC: O(m * n), SC: O(m * n) where m = len(image) and n = len(image[0])
        """
        from collections import deque

        NUM_ROWS = len(image)
        NUM_COLS = len(image[0])
        START_COLOR = image[sr][sc]
        DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def is_inbounds(row, col):
            return 0 <= row < NUM_ROWS and 0 <= col < NUM_COLS

        queue = deque()
        queue.append((sr, sc))
        visited = set()

        while queue:
            row, col = queue.popleft()

            if not is_inbounds(row, col):
                continue

            if image[row][col] != START_COLOR:
                continue

            if (row, col) in visited:
                continue

            image[row][col] = color
            visited.add((row, col))

            for change_row, change_col in DIRECTIONS:
                new_row = row + change_row
                new_col = col + change_col
                queue.append((new_row, new_col))

        return image

class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        """
        TC: O(m * n), SC: O(1) where m = len(matrix) and n = len(matrix[0])
        """
        NUM_ROWS = len(matrix)
        NUM_COLS = len(matrix[0])

        for row in range(1, NUM_ROWS):
            for col in range(1, NUM_COLS):
                if matrix[row][col] != matrix[row - 1][col - 1]:
                    return False

        return True

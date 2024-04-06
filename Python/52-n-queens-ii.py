class Solution:
    def totalNQueens(self, n: int) -> int:
        unavailable_columns = set()
        unavailable_positive_diagonals = set()
        unavailable_negative_diagonals = set()
        STARTING_ROW = 0
        valid_boards = 0

        def count_valid_boards(row):
            nonlocal valid_boards

            if row == n:
                valid_boards += 1
                return

            for col in range(n):
                if col in unavailable_columns:
                    continue
                if row + col in unavailable_positive_diagonals:
                    continue
                if row - col in unavailable_negative_diagonals:
                    continue

                unavailable_columns.add(col)
                unavailable_positive_diagonals.add(row + col)
                unavailable_negative_diagonals.add(row - col)

                count_valid_boards(row + 1)

                unavailable_columns.remove(col)
                unavailable_positive_diagonals.remove(row + col)
                unavailable_negative_diagonals.remove(row - col)

        count_valid_boards(STARTING_ROW)

        return valid_boards

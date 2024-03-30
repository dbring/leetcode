# Definition for a QuadTree node.
class Node:
    def __init__(
        self,
        val,
        isLeaf,
        topLeft=None,
        topRight=None,
        bottomLeft=None,
        bottomRight=None,
    ):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: list[list[int]]) -> Node:
        """
        TC: O(nm), SC: O(log(nm)) where n = len(grid) and m = len(grid[0])
        """

        def construct_quad_tree(start_row, end_row, start_col, end_col):
            if (start_row, start_col) == (end_row - 1, end_col - 1):
                return Node(grid[start_row][start_col], True)

            mid_row = start_row + (end_row - start_row) // 2
            mid_col = start_col + (end_col - start_col) // 2

            top_left = construct_quad_tree(start_row, mid_row, start_col, mid_col)
            top_right = construct_quad_tree(start_row, mid_row, mid_col, end_col)
            bottom_left = construct_quad_tree(mid_row, end_row, start_col, mid_col)
            bottom_right = construct_quad_tree(mid_row, end_row, mid_col, end_col)

            children = (top_left, top_right, bottom_left, bottom_right)
            value = top_left.val

            are_children_leaves = all(child.isLeaf == True for child in children)
            are_children_same_val = all(child.val == value for child in children)

            return (
                Node(value, True)
                if are_children_leaves and are_children_same_val
                else Node(value, False, top_left, top_right, bottom_left, bottom_right)
            )

        num_rows = len(grid)
        num_cols = len(grid[0])

        return construct_quad_tree(0, num_rows, 0, num_cols)

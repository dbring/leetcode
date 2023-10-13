class Solution:
    def trap(self, height: list[int]) -> int:
        max_height = max(height)
        max_index = -1
        total_water = 0

        for i in range(len(height)):
            if height[i] == max_height:
                max_index = i

        left_max = height[0]
        for i in range(1, max_index):
            if height[i] > left_max:
                left_max = height[i]
            else:
                total_water += left_max - height[i]

        right_max = height[-1]
        for i in range(len(height) - 2, max_index, -1):
            if height[i] > right_max:
                right_max = height[i]
            else:
                total_water += right_max - height[i]

        return total_water

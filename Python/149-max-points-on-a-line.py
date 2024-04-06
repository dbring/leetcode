from collections import defaultdict


class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        """
        T:O(n^2) SC: O(n^2)
        """
        if len(points) <= 2:
            return len(points)

        max_points = 0

        def get_slope_and_intercept(p1, p2):
            x1, y1 = p1
            x2, y2 = p2

            if x1 == x2:
                return None, x1

            slope = (y2 - y1) / (x2 - x1)
            intercept = y1 - slope * x1

            return slope, intercept

        for i, p1 in enumerate(points):
            m_and_b = defaultdict(lambda: defaultdict(lambda: 1))

            for p2 in points[i + 1 :]:
                slope, intercept = get_slope_and_intercept(p1, p2)
                m_and_b[slope][intercept] += 1
                max_points = max(max_points, m_and_b[slope][intercept])

        return max_points

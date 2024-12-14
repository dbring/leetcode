class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        """
        TC: O(n), SC:O(1) if you don't count result array, n = len(intervals)
        """
        n = len(intervals)
        i = 0
        new_intervals = []

        while i < n and intervals[i][1] < newInterval[0]:
            new_intervals.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1

        new_intervals.append(newInterval)

        while i < n:
            new_intervals.append(intervals[i])
            i += 1

        return new_intervals

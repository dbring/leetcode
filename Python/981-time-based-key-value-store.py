class TimeMap:
    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        """
        TC: O(1), SC:O(1)
        """
        if key not in self.timemap:
            self.timemap[key] = []

        self.timemap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        """
        TC: O(nlogn), SC: O(1) where n = len(self.timemap.get(key, []))
        """
        VALUES = self.timemap.get(key, [])

        left = 0
        right = len(VALUES) - 1
        found = ""

        while left <= right:
            mid = left + (right - left) // 2

            prev_timestamp = VALUES[mid][0]

            if prev_timestamp <= timestamp:
                found = VALUES[mid][1]
                left = mid + 1

            else:
                right = mid - 1

        return found

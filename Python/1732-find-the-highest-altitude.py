class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        """
        TC: O(n), SC:O(1)
        """
        max_altitude = 0
        current_altitude = 0

        for net_gain in gain:
            current_altitude += net_gain
            max_altitude = max(max_altitude, current_altitude)

        return max_altitude

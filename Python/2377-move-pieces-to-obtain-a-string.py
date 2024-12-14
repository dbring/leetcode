class Solution:
    def canChange(self, start: str, target: str) -> bool:
        """
        TC: O(n), SC:O(1) where n = len(start) = len(target)
        """

        def count_l_and_r(s):
            num_l, num_r = 0, 0

            for char in s:
                if char == "L":
                    num_l += 1
                if char == "R":
                    num_r += 1
            return num_l, num_r

        start_l, start_r = count_l_and_r(start)
        target_l, target_r = count_l_and_r(target)

        if start_l != target_l or start_r != target_r:
            return False

        s = 0
        t = 0
        while s < len(start) and t < len(target):
            if start[s] == "_":
                s += 1
            elif target[t] == "_":
                t += 1
            elif start[s] == "L" and target[t] == "L" and t <= s:
                s += 1
                t += 1
            elif start[s] == "R" and target[t] == "R" and s <= t:
                s += 1
                t += 1
            else:
                return False

        return True

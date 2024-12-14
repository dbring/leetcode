class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        """
        TC: O(m + n), SC: O(m) where n = n, m = len(banned)
        """
        banned = set(banned)
        count = 0
        cur_sum = 0

        for i in range(1, n + 1):
            if i in banned:
                continue

            cur_sum += i

            if cur_sum <= maxSum:
                count += 1
            else:
                return count

        return count

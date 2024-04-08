from collections import deque


class RecentCounter:
    """
    TC: O(1), SC:O(1) since the queue has at most 3000 elements.
    """

    def __init__(self):
        self.recent_requests = deque()
        self.recency = 3000

    def ping(self, t: int) -> int:
        self.recent_requests.append(t)

        while self.recent_requests[0] < t - self.recency:
            self.recent_requests.popleft()

        return len(self.recent_requests)

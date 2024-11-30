class Solution:
    def getAncestors(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        """
        TC: O(n^2logn + E) SC: O(n^2 + E) where n = n and E = len(edges)
        The n^2logn comes from the last loop - n for the loop and nlogn to sort, E from looping over edges.
        The n^2 for space comes from the ancestors list (size n, and each set can also be size n), the E comes from the graph.
        """
        from collections import deque

        queue = deque()
        indegree = [0] * n
        graph = {}
        ancestors = [set() for _ in range(n)]

        for a, b in edges:
            indegree[b] += 1
            ancestors[b].add(a)
            if a not in graph:
                graph[a] = []
            graph[a].append(b)

        for node in range(n):
            if indegree[node] == 0:
                queue.append(node)

        while queue:
            node = queue.popleft()

            neighbors = graph.get(node, [])

            for neighbor in neighbors:
                ancestors[neighbor].update(ancestors[node])
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        result = []
        for node in range(n):
            result.append(sorted(ancestors[node]))

        return result

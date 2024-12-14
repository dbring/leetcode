from collections import deque, defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        TC: O(V + E), SC: O(V + E)
        where V = numCourses and E = len(prerequisites)
        """
        queue = deque()

        def build_graph():
            graph = defaultdict(list)

            for a, b in prerequisites:
                graph[a].append(b)  # a has a directed edge to b

            return graph

        def count_indegrees():
            indegree = [0] * numCourses

            for _, b in prerequisites:
                indegree[b] += 1

            return indegree

        graph = build_graph()
        indegree = count_indegrees()

        for node in range(numCourses):
            if indegree[node] == 0:
                queue.append(node)

        while queue:
            node = queue.popleft()

            neighbors = graph.get(node, [])

            for neighbor in neighbors:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return all(deg == 0 for deg in indegree)

class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        """
        TC: O(n), SC:O(n)
        """

        def build_graph():
            graph = {}

            for a, b in connections:
                if a not in graph:
                    graph[a] = []

                if b not in graph:
                    graph[b] = []

                graph[a].append(b)

            return graph

        graph = build_graph()

        def build_bidirectional_graph():
            bd_graph = {}

            for a, b in connections:
                if a not in bd_graph:
                    bd_graph[a] = []

                if b not in bd_graph:
                    bd_graph[b] = []

                bd_graph[a].append(b)
                bd_graph[b].append(a)

            return bd_graph

        bd_graph = build_bidirectional_graph()
        number_of_reorders = 0
        visited = set([0])

        def visit_cities(city):
            nonlocal number_of_reorders

            neighbors = bd_graph[city]

            for neighbor in neighbors:
                if neighbor in visited:
                    continue

                visited.add(neighbor)

                real_neighbors = graph[city]

                if neighbor in real_neighbors:
                    number_of_reorders += 1

                visit_cities(neighbor)

        visit_cities(0)
        return number_of_reorders

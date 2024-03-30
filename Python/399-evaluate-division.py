def calcEquation(
    self, equations: list[list[str]], values: list[float], queries: list[list[str]]
) -> list[float]:
    """
    TC: O(N*M) SC: O(N) where n = len(equations) and m = len(queries)
    """
    query_answers = []

    def create_graph():
        graph = {}

        for i, equation in enumerate(equations):
            var1, var2 = equation
            value = values[i]

            if var1 not in graph:
                graph[var1] = []

            if var2 not in graph:
                graph[var2] = []

            graph[var1].append([var2, value])
            graph[var2].append([var1, 1 / value])

        return graph

    def solve(current, end, product, visited):
        nonlocal graph

        if current not in graph or end not in graph:
            return -1.0

        if current == end:
            return product

        visited.add(current)

        for neighbor, value in graph[current]:
            if neighbor in visited:
                continue

            res = solve(neighbor, end, product * value, visited)

            if res != -1.0:
                return res

        return -1.0

    graph = create_graph()

    for var1, var2 in queries:
        query_answers.append(solve(var1, var2, 1.0, set()))

    return query_answers

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E', 'A'],
    'C': ['F', 'H', 'A'],
    'D': ['B'],
    'E': ['B', 'G'],
    'F': ['C'],
    'G': ['E'],
    'H': ['C']
}

def DLS(graph, start, goal, limit):
    stack = [(start, [start], 0)]

    while stack:
        node, path, depth = stack.pop()
        print(node)

        if node == goal:
            return path

        if depth < limit:
            for neighbor in graph[node]:
                if neighbor not in path:
                    stack.append((neighbor, path + [neighbor], depth + 1))

    return None


print(DLS(graph, 'A', 'G', 2))

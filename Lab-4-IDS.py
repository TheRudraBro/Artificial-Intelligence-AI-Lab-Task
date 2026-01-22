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

def IDS(graph, start, goal, depth):
    for limit in range(depth + 1):
        stack = [(start, [start], 0)]

        while stack:
            node, path, depth = stack.pop()

            if node == goal:
                return path

            if depth < limit:
                for neighbor in graph[node]:
                    if neighbor not in path:
                        stack.append((neighbor, path + [neighbor], depth + 1))

    return None

print(IDS(graph, 'A', 'G', 2))

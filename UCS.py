import heapq

def ucs(graph, start, goal):
    visited = set()
    priority_queue = [(0, start, [start])]  # (cost, vertex, path)

    while priority_queue:
        cost, vertex, path = heapq.heappop(priority_queue)

        if vertex == goal:
            return path  # Return the path if goal is reached

        if vertex not in visited:
            visited.add(vertex)

            for neighbor, edge_cost in graph[vertex].items():
                if neighbor not in visited:
                    heapq.heappush(
                        priority_queue,
                        (cost + edge_cost, neighbor, path + [neighbor])
                    )

    return None  # Return None if no path is found


# Graph
graph = {
    'a': {'b': 1, 'c': 4},
    'b': {'a': 1, 'd': 2, 'e': 3},
    'c': {'a': 4, 'f': 5},
    'd': {'b': 2},
    'e': {'b': 3},
    'f': {'c': 5}
}

start_node = 'a'
goal_node = 'f'

path = ucs(graph, start_node, goal_node)

if path:
    print("Path from {} to {}: {}".format(start_node, goal_node, " -> ".join(path)))
else:
    print("No path found from {} to {}".format(start_node, goal_node))
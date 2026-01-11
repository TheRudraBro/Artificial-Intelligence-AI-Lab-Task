from collections import deque

def bfs(graph, start):
    queue = deque([start])
    visited = set([start])

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['A', 'B'],
    'D': ['A', 'H'],
    'E': ['B'],
    'F': ['B'],
    'G': ['C'],
    'H': ['D']
}

bfs(graph, 'A')

from collections import deque


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E', 'A'],
    'C': ['F', 'H', 'A'],
    'D': ['M', 'B'],
    'E': ['B', 'G'],
    'F': ['C', 'K'],
    'G': ['E'],
    'H': ['C'],
    'K': ['F'],
    'M': ['D']
}

def bfs(graph, start, goal):
    visited = set()
    queue = deque([start])

    visited.add(start)

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
        if not == goal:
            print("Yeaaaaaaaaaahhhhhhhhhhhhh")
            return

        for neighbor in graph [node]:
            if neighbor not in visited:
                queue.append(neighbor)

bfs(graph,'A', 'G')
    

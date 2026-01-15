from collections import deque

graph = {
    'S':['A', 'B', 'C'],
    'A': ['D', 'E', 'A'],
    'C': ['F', 'H', 'A'],
    'D': ['M', 'B'],
    'E': ['B', 'G'],
    'F': ['K', 'C'],
    'K': ['F'],
    'H':['C']
}

def dfs(graph, start, goal):
    visited = set()
    stack = deque([start])

    while stack:
        node = stack.pop()

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            print("Yeaaaaaaaaaahhhhhhhhhhhhh")
            return

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                stack.append(neighbor)

    print("Goal not found")

dfs(graph, 'S', 'G')

from collections import deque

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

def bfs(graph, start, goal):
    queue = deque([[start]])
    visited = {start}

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            print("Yeaaaaaaaaaahhhhhhhhhhhhh")
            return path

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])
                
    return None 

result = bfs(graph, 'A', 'G')
print(f"{result}")

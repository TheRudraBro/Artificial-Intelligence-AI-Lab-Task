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

def dfs(graph, start, goal):
    stack = deque([[start]])
    visited = {start}

    while stack:
        path = stack.pop() 
        node = path[-1]

        if node == goal:
            print("Yeaaaaaaaaaahhhhhhhhhhhhh")
            return path

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(path + [neighbor])
                
    return None 

result = dfs(graph, 'A', 'G')
print(f"{result}")

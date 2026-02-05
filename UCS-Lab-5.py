import heapq

graph = {
    'M': [('A', 4), ('B', 3), ('C', 2)],
    'A': [('M', 4), ('D', 1)],
    'B': [('M', 3), ('R', 6), ('P', 4)],
    'C': [('M', 2), ('P', 5)],
    'D': [('A', 1), ('R', 2), ('G', 6)],
    'R': [('D', 2), ('B', 6), ('G', 3)],
    'P': [('B', 4), ('C', 5), ('G', 4)],
    'G': [('D', 6), ('R', 3), ('P', 4)]
}

def UCS(graph, start, goal):
    pq = [(0, start, [start])]
    visited = set()

    while pq:
        cost, node, path = heapq.heappop(pq)

        
        if node == goal:
            return cost, path

        
        if node not in visited:
            visited.add(node)

            for neighbor, weight in graph.get(node, []):
                if neighbor not in visited:
                  
                    heapq.heappush(pq, (cost + weight, neighbor, path + [neighbor]))

    return float("inf"), [] 


cost, path = UCS(graph, 'M', 'G')
print({' -> '.join(path)})
print({cost})

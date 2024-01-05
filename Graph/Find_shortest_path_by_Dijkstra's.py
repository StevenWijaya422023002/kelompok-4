import heapq

def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

graph = {
    'A': {'B': 2, 'D': 1},
    'B': {'A': 2, 'C': 5, 'D': 2},
    'C': {'B': 5, 'D': 4},
    'D': {'A': 1, 'B': 2, 'C': 4}
}

start_node = 'A'
result = dijkstra(graph, start_node)

print(f"Jarak terpendek dari {start_node}:")
for node, distance in result.items():
    print(f"{node}: {distance}")

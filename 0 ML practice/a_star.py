import heapq
import sys

def a_star():
    
    data = sys.stdin.read().strip()
    if not data:
        return

    
    parts = data.replace('|', ' ').split()
    
    if len(parts) < 4:
        return

    total_nodes = int(parts[0])
    total_edges = int(parts[1])
    start_node = int(parts[2])
    goal_node = int(parts[3])

   
    current_ptr = 4
    
  
    graph = {i: [] for i in range(total_nodes)}
    for _ in range(total_edges):
        u = int(parts[current_ptr])
        v = int(parts[current_ptr + 1])
        w = int(parts[current_ptr + 2])
        graph[u].append((v, w))
        current_ptr += 3

  
    heuristics = {}
    for i in range(total_nodes):
        heuristics[i] = int(parts[current_ptr])
        current_ptr += 1

   
    pq = [(heuristics[start_node], 0, start_node)]
    visited = {}

    while pq:
        f, g, current = heapq.heappop(pq)

        if current == goal_node:
            print(g) 
            return

        if current in visited and visited[current] <= g:
            continue
        visited[current] = g

        for neighbor, weight in graph.get(current, []):
            new_g = g + weight
            new_f = new_g + heuristics[neighbor]
            heapq.heappush(pq, (new_f, new_g, neighbor))

    print("No path found")

if __name__ == "__main__":
    a_star()
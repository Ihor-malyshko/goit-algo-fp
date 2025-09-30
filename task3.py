import heapq
from collections import defaultdict

class Graph:
    def __init__(self):
        self.vertices = set()
        self.edges = defaultdict(list)
    
    def add_edge(self, u, v, weight):
        self.vertices.add(u)
        self.vertices.add(v)
        self.edges[u].append((v, weight))
        self.edges[v].append((u, weight))
    
    def dijkstra(self, start):
        distances = {vertex: float('infinity') for vertex in self.vertices}
        distances[start] = 0
        previous = {vertex: None for vertex in self.vertices}
        
        priority_queue = [(0, start)]
        visited = set()
        
        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)
            
            if current_vertex in visited:
                continue
                
            visited.add(current_vertex)
            
            for neighbor, weight in self.edges[current_vertex]:
                if neighbor not in visited:
                    distance = current_distance + weight
                    
                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        previous[neighbor] = current_vertex
                        heapq.heappush(priority_queue, (distance, neighbor))
        
        return distances, previous
    
    def get_shortest_path(self, start, end, previous):
        path = []
        current = end
        
        while current is not None:
            path.append(current)
            current = previous[current]
        
        path.reverse()
        return path if path[0] == start else []

def create_sample_graph():
    graph = Graph()
    
    graph.add_edge('A', 'B', 4)
    graph.add_edge('A', 'C', 2)
    graph.add_edge('B', 'C', 1)
    graph.add_edge('B', 'D', 5)
    graph.add_edge('C', 'D', 8)
    graph.add_edge('C', 'E', 10)
    graph.add_edge('D', 'E', 2)
    graph.add_edge('D', 'F', 6)
    graph.add_edge('E', 'F', 3)
    
    return graph

def print_results(graph, start, distances, previous):
    for vertex in sorted(graph.vertices):
        path = graph.get_shortest_path(start, vertex, previous)
        path_str = ' -> '.join(path)
        print(f"до {vertex} ({distances[vertex]}) path: {path_str}")


graph = create_sample_graph()
print("вершини", sorted(graph.vertices))
print("ребра")
for vertex in sorted(graph.vertices):
    for neighbor, weight in graph.edges[vertex]:
        if vertex < neighbor:
            print(f"{vertex} - {neighbor} ({weight})")

start_vertex = 'A'
distances, previous = graph.dijkstra(start_vertex)

print(f"\nвід {start_vertex}")
print_results(graph, start_vertex, distances, previous)

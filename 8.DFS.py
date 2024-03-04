class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbors):
        self.graph[node] = neighbors

def dfs(graph, start, visited):
    if start not in visited:
        print(start, end=" ")
        visited.add(start)
        for neighbor in graph[start]:
            dfs(graph, neighbor, visited)

if __name__ == "__main__":
    # Create a sample graph
    my_graph = Graph()
    my_graph.add_edge('A', ['B', 'C'])
    my_graph.add_edge('B', ['D', 'E'])
    my_graph.add_edge('C', ['F'])
    my_graph.add_edge('D', [])
    my_graph.add_edge('E', ['F'])
    my_graph.add_edge('F', [])

    # Perform DFS starting from node 'A'
    start_node = 'A'
    visited_nodes = set()
    
    print("DFS starting from node", start_node, ":")
    dfs(my_graph.graph, start_node, visited_nodes)

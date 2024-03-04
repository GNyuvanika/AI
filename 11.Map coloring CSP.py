def is_valid(node, color, coloring, graph):
    for neighbor in graph[node]:
        if neighbor in coloring and coloring[neighbor] == color:
            return False
    return True

def color_map(node, colors, coloring, graph):
    if node not in coloring:
        for color in colors:
            if is_valid(node, color, coloring, graph):
                coloring[node] = color
                next_node = get_unassigned_node(coloring, graph)
                if next_node is None or color_map(next_node, colors, coloring, graph):
                    return True
                coloring[node] = None
    return False

def get_unassigned_node(coloring, graph):
    for node in graph:
        if node not in coloring:
            return node
    return None

if __name__ == "__main__":
    # Define the graph (map) and available colors
    graph = {
        'WA': ['NT', 'SA'],
        'NT': ['WA', 'SA', 'Q'],
        'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
        'Q': ['NT', 'SA', 'NSW'],
        'NSW': ['Q', 'SA', 'V'],
        'V': ['SA', 'NSW']
    }

    colors = ['Red', 'Green', 'Blue']

    # Initialize an empty coloring
    coloring = {}

    # Solve the Map Coloring problem
    if color_map('WA', colors, coloring, graph):
        print("Map Coloring Solution:")
        for node, color in coloring.items():
            print(f"{node}: {color}")
    else:
        print("No solution found.")

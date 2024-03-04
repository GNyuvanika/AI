import heapq

class Node:
    def __init__(self, position, parent=None, cost=0, heuristic=0):
        self.position = position
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def calculate_heuristic(current, goal):
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

def astar_search(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_set = []
    closed_set = set()

    start_node = Node(start, None, 0, calculate_heuristic(start, goal))
    heapq.heappush(open_set, start_node)

    while open_set:
        current_node = heapq.heappop(open_set)

        if current_node.position == goal:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]

        closed_set.add(current_node.position)

        for neighbor in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_position = (current_node.position[0] + neighbor[0], current_node.position[1] + neighbor[1])

            if 0 <= new_position[0] < rows and 0 <= new_position[1] < cols and grid[new_position[0]][new_position[1]] == 0 and new_position not in closed_set:
                new_node = Node(new_position, current_node, current_node.cost + 1, calculate_heuristic(new_position, goal))

                if new_node not in open_set:
                    heapq.heappush(open_set, new_node)

    return None  # No path found

if __name__ == "__main__":
    # Example usage
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]

    start_position = (0, 0)
    goal_position = (4, 4)

    path = astar_search(grid, start_position, goal_position)

    if path:
        print("Path found:", path)
    else:
        print("No path found.")

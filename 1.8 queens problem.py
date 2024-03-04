import heapq

class PuzzleNode:
    def __init__(self, state, parent=None, move=None, cost=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.cost = cost

    def __lt__(self, other):
        return (self.cost + self.heuristic()) < (other.cost + other.heuristic())

    def __eq__(self, other):
        return self.state == other.state

    def __hash__(self):
        return hash(tuple(self.state))

    def is_goal(self):
        goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        return self.state == goal_state

    def heuristic(self):
        # Manhattan distance heuristic
        total_distance = 0
        for i in range(9):
            if self.state[i] != 0:
                row_goal = self.state[i] // 3
                col_goal = self.state[i] % 3
                row_current = i // 3
                col_current = i % 3
                total_distance += abs(row_goal - row_current) + abs(col_goal - col_current)
        return total_distance

    def get_neighbors(self):
        neighbors = []
        empty_index = self.state.index(0)

        # Possible moves: left, right, up, down
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for move in moves:
            new_row = empty_index // 3 + move[0]
            new_col = empty_index % 3 + move[1]

            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_state = self.state.copy()
                new_state[empty_index], new_state[new_row * 3 + new_col] = new_state[new_row * 3 + new_col], new_state[empty_index]
                neighbors.append(PuzzleNode(new_state, self, move, self.cost + 1))

        return neighbors

if __name__ == "__main__":
    initial_state = [1, 2, 3, 4, 5, 6, 0, 7, 8]
    
    start_node = PuzzleNode(initial_state)
    open_set = [start_node]
    closed_set = set()

    while open_set:
        current_node = heapq.heappop(open_set)

        if current_node.is_goal():
            path = []
            while current_node:
                path.append((current_node.state, current_node.move))
                current_node = current_node.parent
            solution = list(reversed(path))
            break

        closed_set.add(current_node)

        for neighbor in current_node.get_neighbors():
            if neighbor not in closed_set and neighbor not in open_set:
                heapq.heappush(open_set, neighbor)

    if solution:
        print("Solution found:")
        for step in solution:
            print(step)
    else:
        print("No solution found.")

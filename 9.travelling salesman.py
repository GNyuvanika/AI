from itertools import permutations

def calculate_total_distance(order, distances):
    total_distance = 0
    for i in range(len(order) - 1):
        total_distance += distances[order[i]][order[i + 1]]
    total_distance += distances[order[-1]][order[0]]  # Return to the starting city
    return total_distance

def travelling_salesman_bruteforce(distances):
    cities = list(range(len(distances)))
    min_distance = float('inf')
    best_order = None

    for order in permutations(cities):
        distance = calculate_total_distance(order, distances)
        if distance < min_distance:
            min_distance = distance
            best_order = order

    return best_order, min_distance

if __name__ == "__main__":
    # Example distances between cities
    distances = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    best_order, min_distance = travelling_salesman_bruteforce(distances)

    print("Best order:", best_order)
    print("Minimum distance:", min_distance)

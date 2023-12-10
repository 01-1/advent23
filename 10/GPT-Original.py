def find_farthest_point(grid):
    rows, cols = len(grid), len(grid[0])

    # Find the starting position (S)
    start_position = None
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'S':
                start_position = (i, j)
                break

    # Define directions for moving (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Perform BFS to calculate distances
    distance_matrix = [[-1] * cols for _ in range(rows)]
    distance_matrix[start_position[0]][start_position[1]] = 0

    queue = [start_position]
    while queue:
        current_position = queue.pop(0)

        for direction in directions:
            new_position = (current_position[0] + direction[0], current_position[1] + direction[1])

            # Check if the new position is within bounds and hasn't been visited
            if 0 <= new_position[0] < rows and 0 <= new_position[1] < cols and distance_matrix[new_position[0]][new_position[1]] == -1:
                distance_matrix[new_position[0]][new_position[1]] = distance_matrix[current_position[0]][current_position[1]] + 1
                queue.append(new_position)

    # Find the farthest point
    farthest_distance = max(max(row) for row in distance_matrix)
    return farthest_distance

# Example usage with the provided grid
grid = [
    ".....",
    ".F-7.",
    ".|.L|",
    ".L-J.",
    "....."
]

result = find_farthest_point(grid)
print(result)

def find_farthest_point(grid):
    rows, cols = len(grid), len(grid[0])

    # Find the starting position (S)
    start_position = (-10**10,0)
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'S':
                start_position = (i, j)
                break

    # Define directions for moving (up, down, left, right)
    directions = {
            'S': [(-1, 0), (0, -1)],
            '|': [(-1, 0), (1, 0)],
            '-': [(0, -1), (0, 1)],
            'L': [(-1, 0), (0, 1)],
            'J': [(-1, 0), (0, -1)],
            '7': [(1, 0), (0, -1)],
            'F': [(1, 0), (0, 1)],
                  }

    # Perform BFS to calculate distances
    distance_matrix = [[-1] * cols for _ in range(rows)]
    distance_matrix[start_position[0]][start_position[1]] = 0

    vct = 0
    vis = [['X'] * cols for _ in range(rows)]

    queue = [start_position]
    while queue:
        current_position = queue.pop(0)
        i, j = current_position
        vis[i][j] = grid[i][j]
        vct += 1


        for direction in directions[grid[i][j]]:
            new_position = (current_position[0] + direction[0], current_position[1] + direction[1])
            ii,jj = new_position
            if grid[ii][jj] == '.':
                continue

            # Check if the new position is within bounds and hasn't been visited
            if 0 <= new_position[0] < rows and 0 <= new_position[1] < cols and distance_matrix[new_position[0]][new_position[1]] == -1:
                distance_matrix[new_position[0]][new_position[1]] = distance_matrix[current_position[0]][current_position[1]] + 1
                queue.append(new_position)


    for x in range(rows):

        for y in range(cols):
            if vis[x][y] != 'X':
                break
            vis[x][y] = ' '

        for y in range(cols):
            if vis[x][cols-1-y] != 'X':
                break
            vis[x][cols-1-y] = ' '

    for y in range(cols):

        for x in range(rows):
            if vis[x][y] not in 'X ':
                break

            vis[x][y] = ' '

        for x in range(rows):
            if vis[rows-1-x][y] not in 'X ':
                break
            vis[rows-1-x][y] = ' '

    print('\n'.join(map(lambda x: ''.join(map(str,x)), vis)))


    # Find the farthest point
    farthest_distance = max(max(row) for row in distance_matrix)
    return farthest_distance

# Example usage with the provided grid
grid = [
]
for _ in range(140):
    grid.append(input())

result = find_farthest_point(grid)
print(result)

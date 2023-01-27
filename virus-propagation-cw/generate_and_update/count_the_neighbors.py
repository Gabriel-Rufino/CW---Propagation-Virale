def count_infections(world, x, y):  # Count the amount of infected cells
    if world[x][y] == 2:  # In case of the cell is alredy infected
        counter = -1
    else:   # In case the cell it's not infected
        counter = 0
    for i in [-1, 0, 1]:  # Run the 3x3 matrix of the neighbors and itself
        for j in [-1, 0, 1]:
            xx = x + i  # xx and yy are the positions of the neighborhoods and also itself
            yy = y + j
            # if the values doesn't belongs to the matrix goes to the next case (edge condition)
            if xx < 0 or yy < 0:
                continue
            if xx == len(world):  # ends of x in the matrix (edge condition)
                break
            if yy == len(world[x]):  # ends of y in the matrix (edge condition)
                break
            # Counts the amount of infected cells in the matrix 3x3(neighboors and itself)
            if world[xx][yy] == 2:
                counter = counter + 1
    return counter


def count_cells(world, state):  # Count the amount of a specific state in the world matrix
    counter = 0
    for i in range(len(world)):
        for j in range(len(world[i])):  # Runs the matrix world
            if world[i][j] == state:  # Check if its equal
                counter += 1
    return counter

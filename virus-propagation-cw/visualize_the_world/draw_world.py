def draw_world(world, d, size):
    for i in range(len(world)):  # Runs the matrix
        for j in range(len(world[i])):
            if world[i][j] == 1:  # Healty
                d.create_rectangle(j * size, i * size, (j + 1) * size,
                                   (i + 1) * size, fill="#6495ed")  # Create a rectangle (Parametres: x1, y1, x2, y2, color)
            elif world[i][j] == 2:  # Sick
                d.create_rectangle(j * size, i * size, (j + 1) * size,
                                   (i + 1) * size, fill="#cd5c5c")
            elif world[i][j] == 3:  # Cured
                d.create_rectangle(j * size, i * size, (j + 1) * size,
                                   (i + 1) * size, fill="#3cb371")
            elif world[i][j] == 4:  # Dead
                d.create_rectangle(j * size, i * size, (j + 1) * size,
                                   (i + 1) * size, fill="#696969")
            elif world[i][j] == 5:  # Vaccinated
                d.create_rectangle(j * size, i * size, (j + 1) * size,
                                   (i + 1) * size, fill="pink")
            else:  # Empty
                d.create_rectangle(j * size, i * size, (j + 1) * size,
                                   (i + 1) * size, fill="lightgrey")

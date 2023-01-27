# Function that will update the draw cells of last generation to the new
def update_draw(world, world2, d, size):
    for i in range(len(world)):
        for j in range(len(world[i])):
            if world2[i][j] == 1:  # Stay healthy
                d.create_rectangle(j * size, i * size, (j + 1) * size,
                                   (i + 1) * size, fill="#6495ed")
            if world2[i][j] == 2:  # Gets sick
                d.create_rectangle(j * size, i * size, (j + 1) * size,
                                   (i + 1) * size, fill="#cd5c5c")
            if world2[i][j] == 3:  # Gets cured
                d.create_rectangle(j * size, i * size, (j + 1) * size,
                                   (i + 1) * size, fill="#3cb371")
            if world2[i][j] == 4:  # Dies
                d.create_rectangle(j * size, i * size, (j + 1) * size,
                                   (i + 1) * size, fill="#696969")
            if world2[i][j] == 5:  # Gets Vaccinated
                d.create_rectangle(j * size, i * size, (j + 1) * size,
                                   (i + 1) * size, fill="pink")

import numpy as np
import random


def gen_random_world(width, height, p_infected, p_empty):
    # width --> The amount of columns
    # height --> The amount of rows
    # p_infected --> Probability of a cell being infected
    # p_empty --> Probability of a cell being empty spaces
    world = np.zeros((width, height))  # Generates a matriz with zeros
    
    for i in range(width):  # Runs the whole matrix
        for j in range(height):
            p = random.random()  # Generates value beetween 0 and 1
            if p < p_infected:  # Chance to be infected
                world[i][j] = 2
            # Chance of being empty espace(should be smaller than 0.1)
            elif p_infected < p < p_infected + p_empty:
                world[i][j] = 0
            else:   # Chance of being normal person
                world[i][j] = 1

    return world

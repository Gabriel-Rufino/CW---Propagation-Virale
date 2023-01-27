from random import random
from generate_and_update.count_the_neighbors import *
import numpy as np
from math import sqrt


def next_world(world, chance_to_infect, chance_to_vacinate, death_rate, cure_rate):
    chance_remain_healty = 1 - chance_to_infect
    # Transforms matrix in array to use shape attribute
    world = np.array(world)
    # Creates a matrix with zero values which will be the next generation
    world2 = np.zeros(world.shape)
    for i in range(len(world)):  # Runs the matrix
        for j in range(len(world[i])):

            if world[i][j] == 1:  # Person is Healty
                c = count_infections(world, i, j)
                total_rate = chance_remain_healty ** c  # Total chance of remains healty
                prob = random()
                if prob > total_rate:  # becomes sick
                    world2[i][j] = 2
                else:   # Stays healty
                    vac = random()
                    if vac > chance_to_vacinate:
                        world2[i][j] = 1  # Stays Healty and unvaccinated
                    else:
                        world2[i][j] = 5  # Gets Vacinated

            elif world[i][j] == 0:  # Empty stays empty
                world2[i][j] = 0

            elif world[i][j] == 3:  # Cured Person
                c = count_infections(world, i, j)
                # Total chance of remains cured (Bigger than the Healty person)
                total_rate = sqrt(sqrt(chance_remain_healty ** c))
                prob = random()
                if prob > total_rate:  # Becomes sick
                    world2[i][j] = 2
                else:   # Stays cured
                    vac = random()
                    if vac > chance_to_vacinate:
                        world2[i][j] = 3  # Stays Cured and unvaccinated
                    else:
                        world2[i][j] = 5  # Gets Vaccinated

            elif world[i][j] == 5:  # Vaccinated stays vacinated
                world2[i][j] = 5

            elif world[i][j] == 4:  # Dead stays dead
                world2[i][j] = 4

            elif world[i][j] == 2:  # Person sick
                sick_prob = random()
                if death_rate > sick_prob:  # Probability to die
                    world2[i][j] = 4
                # Probability to cure
                elif death_rate < sick_prob < (cure_rate + death_rate):
                    world2[i][j] = 3
                else:  # Probability to stay sick
                    world2[i][j] = 2

    return world2

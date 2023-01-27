# Virus propagation


## The Group

* Changhao Cai
* Gabriel Rufino Montenegro
* Joao Gabriel Moreira Rocha
* Pierre Fritz
* Viviane de Carvalho Consul
* Zenta Utagawa

## Install

To execute the installation, type the following command on the terminal:

pip install -r requirements.txt

## Execute the simulator

1. Type "python main.py" on the shell.
2. Open the window of the app in full screen.
3. Enter in each entry the corresponding probability (ps,pc,pd and pv).
4. Check if pc + pd < 1 , otherwise the app will crash.
5. Once these steps are completed, press the button UPLOAD MY CHANGES (otherwise, the simulation runs with values set to 0).
6. Press start.
7. If you want to go faster, move the speed cursor to the right.

## Description

A simulation of the propagation of the Spanish flu, considering the probability of being contaminated depending on the interactions between the different states and positions that persons can take. In this simulation, there are six different states for the individuals:

* 0 - Empty space (grey)
* 1 - Healthy person (blue)
* 2 - Infected person (red)
* 3 - Cured person (green)
* 4 - Dead person (black)
* 5 - Vaccinated person (pink)


The users can choose the probabilities of the disease like following:

* for a healthy person to be sick having one neighbor that is sick = ps
* for a sick person to get dead = pd
* for a sick person to get cured = pc
* for a healthy person and a cured to become vaccinated, considering you have not been sick = pv


A healthy person can be infected, or, if a vaccine is implemented, can be vaccinated. After being infected, the person can be cured or dies. A person who is cured or vaccinated cannot be infected. Each probabilities of change are next.

At moment t, we consider that for a single cell the number of sick neighbors is n.

* Empty:

  →　Empty with a probability = 1

* Healthy:

  → Become sick = 1 - (1 - ps)ˆn

  + If the person does not became sick we got two other cases that can happen:

  → Gets Vaccinated with a probability = pv

  → Stays Healty with a probability  = 1 - pv

* Sick:

  → Cured with a probability = pc

  → Dead with a probability = pd

  → Sick with a probability = 1 - pc - pd

* Cured:

  → Become sick with a probabilty = 1 - sqrt(sqrt(1 - ps)ˆn)) Which is less compared to a person that never got sick

  + If the person does not became sick again we got two other cases that can happen:

  → Gets Vaccinated with a probability = pv 

  → Stays Cured with a probability = 1 - pv

* Dead:

  → Dead with a probability = 1

* Vaccinated:

  → Vaccinated with a probability = 1


## Structure of this program

There are the following file:

* count_the_neighbors.py           :To count the number of each types of people
* draw_world.py         :To show the colors of each types of people in the animation
* update_draw           :To update the canvas considering the previous generation
* gen_random_world.py   :To create the initial condition at random
* main.py           :To show the result of the calculation with the graphs and the animations
* next_world.py          :To create the next condition referring to the previous situation with the function of logic.py
* test_functions.py     :To test the each functions with pytest

## How to use the simulator:

The interface is composed with the following elements:
  * Up right, the execution time: it's the time in ms since the user launched the simulation.
  * 2 canvas: the one at left represents the "universe". Within it, you can see the evolution of the state of the people with time. The one at right gives the evolution with time of the proportion of the different types of individuals (healthy, sick, cured, dead, vaccinated).
  * a cursor, under the canvas at right, allowing the user to change the speed of evolution of the universe; allowing him to quickly reach the final state.
  * 2 buttons, start and quit. Start launchs the simulation. Quit allows the user to quit the application.
  * 3 entries to enter the probabilities that are necessary for the simulation. Pay attention not to have pc + pd > 1
  ! Otherwise the program will crash.
  * A descriptive canvas reminding the user which colour is associated with which state.
  * A final entry to enter pv if the user choose to implement a vaccine. By default, pv is set to 0.
  * A button to upload the changes.

## Implemented functions 

* gen_random_world(width, height, p_infected, p_empty):   Creates the initial generation with a certain width and height size and percentage of infected and empty cells.
* count_infections(world, x, y):    Count the amount of infected cells that are next to a cell in a specified position in the matrix. This function is necessary to apply the game rules.
* count_cells(world, state):    Count the amount of cells in a specified state. It will be used as a parameter for the graph.
* draw_world(world, d, size):   Responsible of drawing the cells of the first generation. Parameters are the matrix of the initial world, canvas of where it will be drawed, the size of each cell.
* update_draw(world, world2, d, size):  Responsible of redrawing the cells that have changed by comparing the current generation and the past. Parameters are the past matrix, new matrix, the canvas and the size of the cells
* next_world(gen, chance_to_infect, chance_to_vacinate, death_rate, cure_rate):  Returns the matrix of the next generation according to the rules that we have mentioned before.

## Lien vers le dépot

* git@gitlab-student.centralesupelec.fr:gabriel.montenegro/virus-propagation-cw.git

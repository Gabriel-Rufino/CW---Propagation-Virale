from generate_and_update.gen_random_world import *
from generate_and_update.count_the_neighbors import *
from generate_and_update.next_world import *
from hypothesis import *
import hypothesis.strategies as st
import random

def test_count_infections():
    world = [
        [0, 1, 2, 4, 5, 2, 4],
        [0, 2, 3, 2, 5, 0, 4],
        [4, 1, 2, 4, 5, 1, 2],
        [2, 1, 3, 0, 5, 2, 4],
        [0, 4, 5, 2, 5, 4, 3],
        [0, 2, 3, 2, 2, 0, 1],
        [2, 1, 3, 4, 5, 0, 5]]
    count = [[0]*7 for i in range(7)]
    for i in range(7):
        for j in range(7):
            count[i][j] = count_infections(world, x=i, y=j)
    result = [
        [1, 2, 2, 2, 2, 0, 1],
        [1, 2, 4, 2, 2, 2, 2],
        [2, 3, 2, 2, 2, 2, 1],
        [0, 2, 2, 2, 2, 1, 2],
        [2, 2, 3, 2, 4, 2, 1],
        [2, 1, 3, 2, 2, 1, 0],
        [1, 2, 2, 2, 2, 1, 0]]
    assert count == result


@given(x = st.integers(min_value=0,max_value=6),
    y = st.integers(min_value=0,max_value=6))
def test_count_infections_h(x,y):
    world = [[0, 1, 2, 4, 5, 2, 4],
        [0, 2, 3, 2, 5, 0, 4],
        [4, 1, 2, 4, 5, 1, 2],
        [2, 1, 3, 0, 5, 2, 4],
        [0, 4, 5, 2, 5, 4, 3],
        [0, 2, 3, 2, 2, 0, 1],
        [2, 1, 3, 4, 5, 0, 5]]
    if world[x][y] == 2:
        counter = -1
    else:  
        counter = 0
    for i in [-1, 0, 1]:  
        for j in [-1, 0, 1]:
            xx = x + i  
            yy = y + j
            if xx < 0 or yy < 0:
                continue
            if xx == len(world):  
                break
            if yy == len(world[x]):  
                break
            if world[xx][yy] == 2:
                counter = counter + 1
    actual_conter = count_infections(world,x,y)
    assert actual_conter == counter


def test_count_cells():
    world = [
        [0, 1, 2, 4, 5, 2, 4],
        [0, 2, 3, 2, 5, 0, 4],
        [4, 1, 2, 4, 5, 1, 2],
        [2, 1, 3, 0, 5, 2, 4],
        [0, 4, 5, 2, 5, 4, 3],
        [0, 2, 3, 2, 2, 0, 1],
        [2, 1, 3, 4, 5, 0, 5]]
    assert count_cells(world, state=0) == 8
    assert count_cells(world, state=1) == 6
    assert count_cells(world, state=2) == 13
    assert count_cells(world, state=3) == 5
    assert count_cells(world, state=4) == 9
    assert count_cells(world, state=5) == 8


def test_gen_random_world():
    width, height, p_infected, p_empty = 50, 50, 0.4, 0.1

    random.seed(43)
    test_world = gen_random_world(width, height, p_infected,
                           p_empty).reshape(width*height).tolist()

    random.seed(43)
    answer = []
    for i in range(width*height):
        p = random.random()
        if p < p_infected:
            answer.append(2)
        elif p_infected < p < p_infected + p_empty:
            answer.append(0)
        else:
            answer.append(1)
    assert test_world == answer


@given(width = st.integers(min_value=1,max_value=200),
    height = st.integers(min_value=1,max_value=200),
    p_infected = st.floats(min_value=0,max_value=0.9),
    p_empty = st.floats(min_value=0,max_value=0.1))
def test_gen_random_world_h(width, height, p_infected, p_empty):
    random.seed(42)
    test_world = gen_random_world(width, height, p_infected,
                           p_empty).reshape(width*height).tolist()
    random.seed(42)
    answer = []
    for i in range(width*height):
        p = random.random()
        if p < p_infected:
            answer.append(2)
        elif p_infected < p < p_infected + p_empty:
            answer.append(0)
        else:
            answer.append(1)
    assert test_world == answer


def test():
    test_count_cells()
    test_count_infections()
    test_count_infections_h()
    test_gen_random_world()
    test_gen_random_world_h()

test()

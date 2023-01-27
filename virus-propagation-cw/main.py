from visualize_the_world.draw_world import draw_world
from visualize_the_world.update_draw import update_draw
from generate_and_update.gen_random_world import *
from generate_and_update.count_the_neighbors import *
from generate_and_update.next_world import *
import time
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import matplotlib
from functools import partial
matplotlib.use('TkAgg')


def sum_list(list1, list2):
    res = [elemA + elemB for elemA, elemB in zip(list1, list2)]
    return res


def run():
    """
    Delay in milliseconds, runs the function that keeps updating the data and the graph
    """
    # we must be sure not to treat the cases that don't satisfy the conditions of use
    if root.vr < 0 or root.vr > 1 or root.dr < 0 or root.dr > 1 or root.cr < 0 or root.cr > 1 or root.ir < 0 or root.ir > 1 or (root.dr + root.cr > 1):
        pass
    else:
        root.after(root.reload//root.speed, graph)


def change_speed(speed):
    """
    Change the speed of the game.
    """
    root.speed = int(speed)


def quit_button():
    root.quit()  # finishes the mainloop
    root.destroy()  # prevent a Fatal Python Error


def graph():
    gen2 = next_world(root.grid, root.ir, root.vr,
                      root.dr, root.cr)  # next generation
    # Draw the update draw over the last draw
    update_draw(root.grid, gen2, root.gof_canvas, root.size)
    root.grid = gen2  # updates to the next grid
    # adds the number of cells in the respective lists
    root.empty_cells.append(count_cells(root.grid, 0))
    root.healty_cells.append(count_cells(root.grid, 1))
    root.infected_cells.append(count_cells(root.grid, 2))
    root.cured_cells.append(count_cells(root.grid, 3))
    root.dead_cells.append(count_cells(root.grid, 4))
    root.vacinated_cells.append(count_cells(root.grid, 5))
    # Add number to the list which beggins with 0 (Count 0, 1, 2, 3, ...) which will be the generations
    root.steps.append(len(root.steps))
    # Keeps adding zero to the list to have the same amount of elements as the other lists
    root.zeros_x.append(0)
    # Delay and runs the function graph again (recursive)
    root.after(root.reload//root.speed, graph)
    # _____________________
    # Lists that will store the values that will be ploted on the stack area graph
    root.a1 = sum_list(root.empty_cells, root.healty_cells)
    root.a2 = sum_list(root.a1, root.infected_cells)
    root.a3 = sum_list(root.a2, root.cured_cells)
    root.a4 = sum_list(root.a3, root.dead_cells)
    root.a5 = sum_list(root.a4, root.vacinated_cells)
    # _____________________
    # Defines x and y data of the lines that will be ploted
    root.line0.set_ydata(root.empty_cells)
    root.line0.set_xdata(root.steps)
    root.line1.set_ydata(root.a1)
    root.line1.set_xdata(root.steps)
    root.line2.set_ydata(root.a2)
    root.line2.set_xdata(root.steps)
    root.line3.set_ydata(root.a3)
    root.line3.set_xdata(root.steps)
    root.line4.set_ydata(root.a4)
    root.line4.set_xdata(root.steps)
    root.line5.set_ydata(root.a5)
    root.line5.set_xdata(root.steps)
    # _____________________________________
    # Color between the lines that are ploted according the colors that represents each state
    root.axes.fill_between(root.steps, root.zeros_x, root.empty_cells, color='lightgrey',
                           alpha=1)
    root.axes.fill_between(root.steps, root.empty_cells, root.a1, color='#6495ed',
                           alpha=1)
    root.axes.fill_between(root.steps, root.a1, root.a2, color='#cd5c5c',
                           alpha=1)
    root.axes.fill_between(root.steps, root.a2, root.a3, color='#3cb371',
                           alpha=1)
    root.axes.fill_between(root.steps, root.a3, root.a4, color='#696969',
                           alpha=1)
    root.axes.fill_between(root.steps, root.a4, root.a5, color='pink',
                           alpha=1)
    # Limits the graphic, 0 to the current amount of generation
    root.axes.set_xlim(0, len(root.steps)-1)
    # Limits the graphic, 0 to the total amount of cells in the first generation which will be the same over time
    root.axes.set_ylim(
        0, root.empty_cells[0] + root.healty_cells[0] + root.infected_cells[0])
    # Function of the interactive mode the draws again with the new data
    root.fig.canvas.draw()
    # When the current generation is divided by 10 the number execution time will be ploted on the screen
    if root.steps[-1] % 10 == 0:
        # Calcules the time (Currente time - time it started)
        s = int(1000*(time.time()-root.start_time))
        root.label["text"] = "Execution Time : {} milliseconds".format(
            s)  # Keeps showing the time on the screen


def ploting():
    root.wm_title("Viral Propagation")  # Title of the screen

    root.label = tk.Label(master=root, text="Execution Time : {} milliseconds".format(
        int(1000*(time.time()-root.start_time))))  # Plots the operation time (Current time - time it started)
    root.label.grid(column=1, row=0)  # Tells where the time will be ploted

    root.speed_slider = tk.Scale(
        root, from_=1, to=10, orient=tk.HORIZONTAL, label='Speed', command=change_speed)  # Calls the slider which is responsible to change the speed
    root.speed_slider.set(root.speed)
    # Tells where the slider will be ploted
    root.speed_slider.grid(column=1, row=3)

    button = tk.Button(master=root, text="Quit",
                       command=quit_button)  # Calls the Quit buttom
    button.grid(column=0, row=4)  # Tells where the quit buttom will be ploted

    # Start call the func "run" which is responsible to initialize the graph function
    root.start_button = tk.Button(master=root, text='Start', command=run)
    # Tells where the start buttom will be ploted
    root.start_button.grid(column=0, row=3)

    # Total width (Total of coluns * Size of the cells)
    root.width = len(root.grid[0]) * root.size
    # Total height (Total of rows * Size of the cells)
    root.height = len(root.grid) * root.size
    root.gof_canvas = tk.Canvas(
        root, width=root.width, height=root.height)  # Creates the big block
    # Tells that the block will be ploted on the left,
    root.gof_canvas.grid(column=0, row=2)
    # Draw the cells with the(Matrix, big block, size of each cell)
    draw_world(root.grid, root.gof_canvas, root.size)

    plt.ion()  # Enable iteractive mode
    # Creates the figure (Width, height in inches.)(The resolution of the figure is in dots-per-inch.)
    root.fig = Figure(figsize=(5, 4), dpi=100)
    # Creates lists which counts the amount of cells of each state and stores the current value
    root.empty_cells = [count_cells(root.grid, 0)]
    root.healty_cells = [count_cells(root.grid, 1)]
    root.infected_cells = [count_cells(root.grid, 2)]
    root.cured_cells = [count_cells(root.grid, 3)]
    root.dead_cells = [count_cells(root.grid, 4)]
    root.vacinated_cells = [count_cells(root.grid, 5)]

    # creates a list that will count the amount of generations
    root.steps = [0]
    # creates a list of just zeros that will be used to fill colors in the stacked area graph
    root.zeros_x = [0]
    # (nº rows, nº cols, top-left position)
    root.axes = root.fig.add_subplot(111)

    # Sum a list values with a list values that were alredy ploted
    # That is a way we found out to be possible to use the stacked area graph
    root.a1 = sum_list(root.empty_cells, root.healty_cells)
    root.a2 = sum_list(root.a1, root.infected_cells)
    root.a3 = sum_list(root.a2, root.cured_cells)
    root.a4 = sum_list(root.a3, root.dead_cells)
    root.a5 = sum_list(root.a4, root.vacinated_cells)

    # Plot invisible lines point to point (Number of alive cells) (Need to be ploted so we can color between then)
    root.line0, = root.axes.plot(root.empty_cells, color="lightgrey", alpha=0)
    root.line1, = root.axes.plot(root.a1, color="#6495ed", alpha=0)
    root.line2, = root.axes.plot(root.a2, color="#cd5c5c", alpha=0)
    root.line3, = root.axes.plot(root.a3, color="#3cb371", alpha=0)
    root.line4, = root.axes.plot(root.a4, color="#696969", alpha=0)
    root.line5, = root.axes.plot(root.a5, color="pink", alpha=0)

    # tkinter drawing area
    root.plt_canvas = FigureCanvasTkAgg(root.fig, master=root)
    root.plt_canvas.draw()
    root.plt_canvas.get_tk_widget().grid(column=1, row=2)


def simulate():
    root.size = 20  # Size of each cell
    root.reload = 1000  # milliseconds to reload the new generation
    root.speed = 1  # Sets the initial speed

    # creating the main window that the user will use

    # Defining all of the parameters and entries that the user will enter
    probability_of_being_sick_having_one_neighbor_that_is_sick = tk.DoubleVar(
        root)
    probability_of_being_cured_after_being_sick = tk.DoubleVar(root)
    probability_to_get_dead_after_being_sick = tk.DoubleVar(root)
    probability_to_get_vaccinated_if_the_person_is_healthy = tk.DoubleVar(root)

    # Explaining the rules
    labelDescription = tk.Label(
        root, text='        To simulate a pandemic, you need to define the parametersdescribed below. You have the possibility to add a vaccine to your simulation.', font=('Calibri', 11))
    labelDescription.grid(column=0, row=6)
    Warningmessage = tk.Label(
        root, text='THE SUM OF THE PROBABILITIES OF BEING CURED AND TO GET DEAD MUST BE LESS THAN 1 !', font=('Calibri', 11))
    Warningmessage.grid(column=1, row=6)

    ps = tk.Label(
        root, text='The probability for a healthy person of being sick having a neighbor that is sick (a float >0 and <1)', relief='groove')
    ps.grid(column=0, row=7)
    probsick = tk.Entry(
        root, textvariable=probability_of_being_sick_having_one_neighbor_that_is_sick, insertbackground='#cd5c5c')
    probsick.grid(column=1, row=7)

    pc = tk.Label(
        root, text='The probability for a sick person of being cured (a float >0 and <1)', relief='groove')
    pc.grid(column=0, row=8)
    probcured = tk.Entry(
        root, textvariable=probability_of_being_cured_after_being_sick, insertbackground='#3cb371')
    probcured.grid(column=1, row=8)

    pd = tk.Label(
        root, text='The probability for a sick person to get dead (a float >0 and <1)', relief='groove')
    pd.grid(column=0, row=9)
    probdead = tk.Entry(
        root, textvariable=probability_to_get_dead_after_being_sick, insertbackground='#696969')
    probdead.grid(column=1, row=9)

    # Additional option: adding a vaccine and parametrizing the probability for a healthy person to get vaccinated
    option = tk.Label(
        root, text='If you want to add a vaccine to your simulation, you can choose the probability for a healthy person to get vaccinated.', relief='groove')
    option.grid(column=0, row=11)
    pv = tk.Label(
        root, text='Choose here this probability (a float <=1). If no vaccine, fill with 0', relief='groove')
    pv.grid(column=0, row=12)
    probvac = tk.Entry(
        root, textvariable=probability_to_get_vaccinated_if_the_person_is_healthy, insertbackground='#6495ed')
    probvac.grid(column=1, row=12)

    # In a canvas, the description to associate a color to a state
    descriptiveCanvas = tk.Canvas(root, background='grey',
                                  height=70, width=360)
    descriptiveCanvas.grid(column=0, row=10)
    descriptiveCanvas.create_rectangle(
        (10, 10), (50, 50), fill='#6495ed')
    descriptiveCanvas.create_text(30, 60, text='Healthy')

    descriptiveCanvas.create_rectangle(
        (70, 10), (110, 50), fill='#cd5c5c')
    descriptiveCanvas.create_text(90, 60, text='sick')

    descriptiveCanvas.create_rectangle(
        (130, 10), (170, 50), fill='#3cb371')
    descriptiveCanvas.create_text(150, 60, text='cured')

    descriptiveCanvas.create_rectangle(
        (190, 10), (230, 50), fill='#696969')
    descriptiveCanvas.create_text(210, 60, text='dead')

    descriptiveCanvas.create_rectangle(
        (250, 10), (290, 50), fill='pink')
    descriptiveCanvas.create_text(270, 60, text='vaccinated')

    descriptiveCanvas.create_rectangle(
        (310, 10), (350, 50), fill='lightgrey')
    descriptiveCanvas.create_text(330, 60, text='empty')

    # adding a button to update the parameters that the user uploaded

    def update():
        probability_of_being_sick_having_one_neighbor_that_is_sick.set(
            probability_of_being_sick_having_one_neighbor_that_is_sick.get())
        probability_of_being_cured_after_being_sick.set(
            probability_of_being_cured_after_being_sick.get())
        probability_to_get_dead_after_being_sick.set(
            probability_to_get_dead_after_being_sick.get())
        probability_to_get_vaccinated_if_the_person_is_healthy.set(
            probability_to_get_vaccinated_if_the_person_is_healthy.get())
        root.vr = probability_to_get_vaccinated_if_the_person_is_healthy.get()
        root.dr = probability_to_get_dead_after_being_sick.get()
        root.cr = probability_of_being_cured_after_being_sick.get()
        root.ir = probability_of_being_sick_having_one_neighbor_that_is_sick.get()
        if root.vr < 0 or root.vr > 1:
            errormessage = tk.Label(
                root, text='ERROR: WATCH THE CONDITIONS ! UPDATE AGAIN.', relief='groove', bg='red')
            errormessage.grid(column=1, row=10)
        if root.dr < 0 or root.dr > 1:
            errormessage = tk.Label(
                root, text='ERROR: WATCH THE CONDITIONS ! UPDATE AGAIN.', relief='groove', bg='red')
            errormessage.grid(column=1, row=10)
        if root.cr < 0 or root.cr > 1:
            errormessage = tk.Label(
                root, text='ERROR: WATCH THE CONDITIONS ! UPDATE AGAIN.', relief='groove', bg='red')
            errormessage.grid(column=1, row=10)
        if root.ir < 0 or root.ir > 1:
            errormessage = tk.Label(
                root, text='ERROR: WATCH THE CONDITIONS ! UPDATE AGAIN.', relief='groove', bg='red')
            errormessage.grid(column=1, row=10)
        if root.dr + root.cr > 1:
            errormessage = tk.Label(
                root, text='ERROR: WATCH THE CONDITIONS ! UPDATE AGAIN.', relief='groove', bg='red')
            errormessage.grid(column=1, row=10)
    button = tk.Button(root, text='UPDATE YOUR CHANGES',
                       command=partial(update))
    button.grid(column=1, row=13)

    root.grid = gen_random_world(20, 20, 0.1, 0.05)
    root.start_time = time.time()

    ploting()  # Function that will animate and plot the simulation on the screen

    tk.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    simulate()


total = root.empty_cells[0] + root.healty_cells[0] + root.infected_cells[0]
print(f'Empty percentage: {root.empty_cells[-1]/total}')
print(f'Healty percentage: {root.healty_cells[-1]/total}')
print(f'Infected percentage: {root.infected_cells[-1]/total}')
print(f'Cured percentage: {root.cured_cells[-1]/total}')
print(f'Dead percentage: {root.dead_cells[-1]/total}')
print(f'Vaccinated percentage: {root.vacinated_cells[-1]/total}')

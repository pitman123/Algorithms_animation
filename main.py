# Main program for generating algorithm animations

import random
import matplotlib.pyplot as plt

from plots import camera
from selectionsort import selection_sort
from quicksort import quick_sort
from bubblesort import bubble_sort
from heapsort import heap_sort

# Set of all algorithms functions
all_func_alg = {'1': selection_sort,
                '2': quick_sort,
                '3': bubble_sort,
                '4': heap_sort,
                }


def main_set(alg, alg_type):
    # titles(alg_type)  # Set plot's title

    func = all_func_alg[alg]  # Set the algorithm to show

    # Set the appropriate type of plot
    if a in ('1', '3', '4'):
        if alg_type == '1':
            func(arr, 'bar')
        elif alg_type == '2':
            func(arr, 'scatter')
    elif a == '2':
        if alg_type == '1':
            func(arr, 0, len(arr) - 1, 'bar')
        elif alg_type == '2':
            func(arr, 0, len(arr) - 1, 'scatter')


if __name__ == '__main__':

    a = input("""Select algorithms: 
                1 - Select Sort
                2: Quick Sort,
                3: Bubble Sort,
                4: Heap Sort""")

    typ = input('Select plot: 1: bar, 2: scatter')

    arr = random.sample(range(30), 30)  # Create random arr

    # Save animation as gif
    # Install imagemagick: https://imagemagick.org/script/download.php
    save = input('Do you want to save? [y/n]: ')

    # set interval time for animation
    interval_time = 200
    animation = camera.animate(interval=interval_time)

    if save == 'y':
        animation.save('algorithms.gif', dpi=60, writer='imagemagick')

    main_set(a, typ)
    plt.show()

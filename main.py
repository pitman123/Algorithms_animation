import random
import matplotlib.pyplot as plt
from plots import camera, titles
from selectionsort import selection_sort
from quicksort import quick_sort
from bubleesort import bubble_sort
from heapsort import heap_sort

alg = {'1': selection_sort,
       '2': quick_sort,
       '3': bubble_sort,
       '4': heap_sort}

a = input('''
            1: Selection Sort 
            2: Quick Sort 
            3: Bubble Sort
            4: Heap Sort 
            Select algorithms: 
            ''')

typ = input('''
            1: bar
            2: scatter  
            Select plot:
            ''')

arr = random.sample(range(30), 30)    # Create random arr

# Set the chart title
titles(a)

func = alg[a]

if a in ('1', '3', '4'):
    if typ == '1':
        func(arr, "bar")
    elif typ == '2':
        func(arr, 'scatter')
elif a == '2':
    if typ == '1':
        func(arr, 0, len(arr)-1, "bar")
    elif typ == '2':
        func(arr, 0, len(arr)-1, 'scatter')

interval_time = 200
animation = camera.animate(interval=interval_time)

# Save animation as gif
# Install imagemagick: https://imagemagick.org/script/download.php
save = input("Do you want to save? [y/n]: ")

if save == 'y':
    animation.save('algorithms.gif', dpi=60, writer='imagemagick')

plt.show()


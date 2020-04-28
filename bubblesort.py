# Python program for implementation of Bubble Sort

from plots import plot


def bubble_sort(arr, type_plot):
    # Traverse through all array elements
    for l in range(len(arr)):
        # Compare all elements
        for i in range(len(arr)):

            if i < (len(arr)) - 1:
                # Swap if the element found is greater
                # than the next element
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]

                    # Created typ with selected plot type
                    plot(arr=arr, fallow_point=i+1, type_plot=type_plot, title='Bubble Sort')

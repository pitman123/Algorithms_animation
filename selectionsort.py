# Python program for implementation of Selection Sort

from plots import plot


def selection_sort(arr, type_plot):
    # Run through all data elements
    for i in range(len(arr)):
        # Find the minimum element
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j

        # Swap the found minimum element with
        # the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

        # Created typ with selected plot type
        plot(arr=arr, fallow_point=min_idx, type_plot=type_plot)


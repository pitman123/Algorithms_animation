# Python program for implementation of heap Sort
# Source: https://www.geeksforgeeks.org/python-program-for-heap-sort/

from plots import plot


def heapify(arr, n, i, type_plot):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

        # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest,  type_plot)

        plot(arr=arr, fallow_point=largest, type_plot=type_plot, title='Heap Sort')


# The main function to sort an array of given size
def heap_sort(arr, type_plot):
    n = len(arr)

    # Build a maxheap
    for i in range(n, -1, -1):
        heapify(arr, n, i,  type_plot)

        # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0, type_plot)
    return arr



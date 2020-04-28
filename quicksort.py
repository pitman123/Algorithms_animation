# Python program for implementation of QuickSort Sort

from plots import plot


# Function to find pivot and
# dividing the arr
def partition(arr, left, right, type_plot):
    i = (left - 1)  # smaller element
    pivot = arr[right]  # pivot

    for j in range(left, right):

        # Swap if current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

            # Create plot with arr and pivot
            plot(arr=arr, fallow_point=pivot, type_plot=type_plot, title='Quick Sort ')

    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1


# Function to do Quick sort
def quick_sort(arr, left, right, type_plot):
    if left < right:
        # return the pivot index
        pi = partition(arr, left, right, type_plot)

        # Separately sort elements before
        # partition and after partition
        quick_sort(arr, left, pi - 1, type_plot)
        quick_sort(arr, pi + 1, right, type_plot)

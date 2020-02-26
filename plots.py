from celluloid import Camera
import matplotlib.pyplot as plt

title = {'1': "Select Sort",
         '2': "Quick Sort",
         '3': 'Bubble Sort',
         '4': 'Heap Sort'}


# Setting the title to the chart
def titles(a):
    global title
    title = title[a]
    return title


# Plot settings and fallow point
fig = plt.figure()
camera = Camera(fig)
base = 0


def plot(arr, fallow_point, type_plot):
    global base

    if type_plot == 'bar':
        colors = list(len(arr) * 'b')
        colors[fallow_point] = 'r'
        plt.bar(range(len(arr)), arr, color=colors)

    elif type_plot == 'scatter':
        plt.scatter(range(len(arr)), arr, c=arr, cmap='nipy_spectral')

    plt.title(title)

    camera.snap()


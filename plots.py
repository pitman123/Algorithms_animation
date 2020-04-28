# Main settings for plots

import matplotlib.pyplot as plt

from celluloid import Camera

# Plot settings and fallow point
fig = plt.figure()
camera = Camera(fig)
base = 0


def plot(arr, fallow_point, type_plot, title):
    global base

    if type_plot == 'bar':
        colors = list(len(arr) * 'b')
        colors[fallow_point] = 'r'
        plt.bar(range(len(arr)), arr, color=colors)

    elif type_plot == 'scatter':
        plt.scatter(range(len(arr)), arr, c=arr, cmap='nipy_spectral')

    plt.title(title)

    camera.snap()

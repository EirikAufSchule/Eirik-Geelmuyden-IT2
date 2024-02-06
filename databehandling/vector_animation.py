"""Fra https://medium.com/@satyamgaikwad92/visualizing-and-animating-vectors-transformations-with-matplotlib-3c4ca3120d6b """

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

pvectors = []
# define function to plot vector
def plot_vector(origin,vector):
    pvectors.append([origin,vector])
    return ax1.quiver(origin[0], origin[1], vector[0], vector[1], angles='xy', scale_units='xy', scale=1, color=np.random.rand(10, 3), label='Vector 1')

#define function to animate/visualize vector
def animate_vector(start,end):
    line = ax1.quiver(start[0], start[1], end[0], end[1], angles='xy', scale_units='xy', scale=1, color=np.random.rand(10, 3), label='Vector 1')
    def update(frame):
        x = np.linspace(start[0],end[0])
        y = np.linspace(start[1],end[1])
        line.set_UVC(x[frame],y[frame])
        return line,
    ani = FuncAnimation(fig, update, frames=100, interval=50, blit=False)
    plt.show()

fig, ax1 = plt.subplots()

axis_size  = 20
# Set the limits of the plot
ax1.set_xlim([-axis_size, axis_size])
ax1.set_ylim([-axis_size, axis_size])

ax1.grid(True)
ax1.axhline(0, color='black', linewidth=0.5)
ax1.axvline(0, color='black', linewidth=0.5)
ax1.set_xlabel('X-axis')
ax1.set_ylabel('Y-axis') 

#define origin and random vector
origin = np.array([0,0])
vector = np.array([2,-9])
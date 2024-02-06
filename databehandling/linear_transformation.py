import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
def lin_transform(matrix, vector):
    x = vector[0]*matrix[0][0] + vector[1]*matrix[1][0]
    y = vector[0]*matrix[0][1] + vector[1]*matrix[1][1]
    return x,y
    
def transform_steps(matrix, frames_count):
    start_matrix = [[1,0], [0,1]]
    a = np.linspace(start_matrix[0][0], matrix[0][0], frames_count)
    b = np.linspace(start_matrix[1][0], matrix[1][0], frames_count)
    c = np.linspace(start_matrix[0][1], matrix[0][1], frames_count)
    d = np.linspace(start_matrix[1][1], matrix[1][1], frames_count)
    return [[a, b], [c,d]]
    
def animate_transformation(vector, matrix, frames_count):
    origin = [0,0]
    line = ax1.quiver(*origin, *vector, angles='xy', scale_units='xy', scale=1, color=np.random.rand(10, 3), label='Vector 1')
    x, y = lin_transform(transform_steps(matrix, frames_count), vector)
    print(x,y)
    def update(frame):
        line.set_UVC(x[frame],y[frame])
        return line,

    ani = FuncAnimation(fig, update, frames=frames_count, interval=20, blit=False, repeat=False)
    plt.show()

# Create a figure and axis
fig, ax1 = plt.subplots()

axis_size  = 40
# Set the limits of the plot
ax1.set_xlim([-axis_size, axis_size])
ax1.set_ylim([-axis_size, axis_size])

ax1.grid(True)
ax1.xlabel("$x$") # $ for LaTex skrift
plt.ylabel("$y$")
ax1.axhline(0, color='black', linewidth=0.5)
ax1.axvline(0, color='black', linewidth=0.5)
ax1.set_xlabel('X-axis')
ax1.set_ylabel('Y-axis') 

#define origin and random vector
origin = np.array([0,0])
vector = np.array([-1,3])
#test
#plotting individual vectors

#animate individual vector
matrix = [[-0.5,-1], [2,3]]

animate_transformation(vector, matrix, 100)


import sys
import os

# we add the ~/matnimation directory to be able to import the 'src' module
sys.path.append(os.path.abspath(''))              

import matplotlib.colors as colors
import numpy as np
from src.matnimation.animation.animation import Animation
from src.matnimation.canvas.single_canvas import SingleCanvas
from src.matnimation.artist.animated.animated_quiver import AnimatedQuiver
from src.matnimation.helper.helper_functions import HelperFunctions as hf

# generate time array
t_array = np.linspace(0, 2*np.pi, 61)

# boundaries and spacing in x and y directions
xmin, xmax, Nx = -1, 1, 10
ymin, ymax, Ny = -1, 1, 10

# arrays for x and y
x_array = np.linspace(xmin, xmax, Nx)
y_array = np.linspace(ymin, ymax, Ny)

# x and y coordinates of rectangular grid
x_grid, y_grid = hf.xy_grid(x_array, y_array)

def funcFx(x,y,t):
    return np.cos(t)

def funcFy(x,y,t):
    return np.sin(t)

Fx_data, Fy_data = hf.FxFy_to_grid(funcFx, funcFy, x_grid, x_grid, t_array)

canvas = SingleCanvas(
    (4,4.5),
    300,
    time_array = t_array, 
    axis_limits = [-1.2,1.2,-1.2,1.2],
    axis_labels= [None, None] 
)

canvas.set_axis_properties(aspect = 'equal')

quiver = AnimatedQuiver('Vector Field', x_grid, y_grid, Fx_data, Fy_data, scale = 20)
canvas.add_artist(quiver)
quiver.set_styling_properties(edgecolor = 'tab:blue', facecolor = colors.to_rgba('tab:blue'))

animation = Animation(canvas, interval = 30)
animation.render('examples/rotating_vectors/rotating_vectors.mp4')
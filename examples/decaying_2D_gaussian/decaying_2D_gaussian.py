import sys
import os

# we add the ~/matnimation directory to be able to import the 'src' module
sys.path.append(os.path.abspath(''))              

import matplotlib.colors as colors
import numpy as np
from src.matnimation.animation.animation import Animation
from src.matnimation.artist.animated.animated_imshow import AnimatedImshow
from src.matnimation.artist.static.static_colorbar import StaticColorBar
from src.matnimation.canvas.single_canvas import SingleCanvas

def gauss(x,y,t,tau):
    return np.exp(-x**2-y**2 - t/tau)

tmin, tmax, Nt = 0, 1, 60
time_array = np.linspace(tmin, tmax, Nt)

# exponential decay constant
tau = 0.5

xmin, xmax, Nx = -2, 2, 200
ymin, ymax, Ny = -2, 2, 200
x_array, y_array = np.linspace(xmin, xmax, Nx), np.linspace(ymin, ymax, Ny)

X, Y = np.meshgrid(x_array, y_array)

image_data = [gauss(X,Y,t,tau) for t in time_array]

canvas = SingleCanvas(
    figsize = (4.5,5.5),
    dpi = 400,
    time_array = time_array,
    axis_limits = [xmin, xmax, ymin, ymax],
    axis_labels = ['$x$','$y$']
)

density = AnimatedImshow(
    name = 'Decaying gaussian', 
    image_data = image_data, 
    extent = [xmin, xmax, ymin, ymax],
    vmin = 0,
    vmax = 1
    )

colorscale = StaticColorBar(
    name = 'Colorbar',
    imshow = density,
    styling_dict = dict(location = 'bottom', orientation = 'horizontal', label = '$\\varphi(x,y)$', ticks = np.linspace(0,2,5))

)

canvas.add_artist(density)
canvas.add_artist(colorscale)

animation = Animation(canvas, interval = 30)

animation.render('examples/decaying_2D_gaussian/decaying_2D_gaussian.mp4')
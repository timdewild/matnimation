import sys
import os

# we add the ~/matnimation directory to be able to import the 'src' module
sys.path.append(os.path.abspath(''))              

import matplotlib.colors as colors
import numpy as np
from src.matnimation.animation.animation import Animation
from src.matnimation.canvas.single_canvas import SingleCanvas
from src.matnimation.artist.animated.animated_scatter import AnimatedScatter
from src.matnimation.helper.helper_functions import HelperFunctions as hf

# animation to simulate travelling sine waves in the x-direction of the form A*sin(k*x - omega*t)

# descretize space (x) and time (t)
Nx = 50
Nt = 50
x_array = np.linspace(0, 2*np.pi, Nx)
t_array = np.linspace(0, 2*np.pi, Nt)

x_data = x_array

# function inside function

def sin(x,t):
    return np.sin(x-t)



y_data = hf.func_ab_to_grid(sin, x_array, t_array)

canvas = SingleCanvas((4,4), 400, t_array, [0,2*np.pi,-1,1], ['$x$','$y$'])

sine1 = AnimatedScatter('$\\sin(x)$', x_data, y_data)
canvas.add_artist(sine1, in_legend = True)
sine1.set_styling_properties(markeredgecolor = 'tab:blue', markerfacecolor = colors.to_rgba('tab:blue', 0.4))


sine2 = AnimatedScatter(r"$\frac{1}{2}\sin(x)$", x_data, 0.5*y_data,)
canvas.add_artist(sine2, in_legend = True)
sine2.set_styling_properties(markeredgecolor = 'tab:red', markerfacecolor = colors.to_rgba('tab:red', 0.4))

canvas.construct_legend(loc = 'upper right')

sines_animation = Animation(canvas)
sines_animation.render('examples/travelling_waves/travelling_waves.mp4')          
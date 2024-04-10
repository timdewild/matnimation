import numpy as np
import sys
import os

# to be able to find ~/matnimation directory
sys.path.append(os.path.abspath(''))

from src.matnimation.animation.animation import Animation
from src.matnimation.canvas.single_canvas import SingleCanvas
from src.matnimation.artist.animated.animated_line import AnimatedLine
from src.matnimation.helper.helper_functions import HelperFunctions

M, N = 1000, 100
x_array = np.linspace(0, 4, M) 
t_array = np.linspace(0, 1, N)

def wave(x,t):
    """Returns the traveling waveform y(x,t) = sin(kx - wt) with k = 2pi and w = 4pi."""
    y = np.sin(2 * np.pi * (x - 2*t)) 
    return y

ydata = HelperFunctions.func_ab_to_grid(
    func = wave,
    a = x_array,
    b = t_array
    )

canvas = SingleCanvas(
    figsize = (6.4, 4.8),
    dpi = 400,
    time_array = t_array,
    axis_limits = [0, 4, -2, 2],
    axis_labels = ['$x$', '$y(x,t)$']
)

travelling_wave = AnimatedLine(
    name = 'Travelling Wave',
    x_data = x_array,
    y_data = ydata,
)

canvas.add_artist(travelling_wave)

animation = Animation(canvas, interval = 20)
animation.render('examples/travelling_sine_wave/travelling_sine_wave_animation.mp4')

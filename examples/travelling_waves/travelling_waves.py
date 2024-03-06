import sys
import os

# we add the ~/matnimation directory to be able to import the 'src' module
sys.path.append(os.path.abspath(''))              

import matplotlib.colors as colors
import numpy as np
from src.matnimation.animation.animation import Animation
from src.matnimation.canvas.single_canvas import SingleCanvas
from src.matnimation.artist.animated.animated_line import AnimatedLine
from src.matnimation.helper.helper_functions import HelperFunctions as hf

# animation to simulate travelling sine waves in the x-direction of the form Psi = A*sin(k*x - omega*t)

# descretize space (x) and time (t)
Nx = 100
Nt = 50
x_array = np.linspace(0, 2*np.pi, Nx)
t_array = np.linspace(0, 2*np.pi, Nt)

# for all animated travelling waves, we take the x_data to be the same
x_data = x_array

def travelling_wave(x, t, amplitude = 1, wavenumber = 1, omega = 1):
    return amplitude * np.sin(wavenumber * x - omega * t)

# y_data for all waves: columns represent the waveform at all x-values at specific timestep.
A1, k1, w1 = 1, 1, 1
y_data_wave1 = hf.func_ab_to_grid(travelling_wave, x_array, t_array, amplitude = A1, wavenumber = k1, omega = w1)
label_wave1 = f"$\\Psi$ ($A={A1}$, $k={k1}$,$\\omega={w1}$)"

A2, k2, w2 = 0.5, 1, 2
y_data_wave2 = hf.func_ab_to_grid(travelling_wave, x_array, t_array, amplitude = A2, wavenumber = k2, omega = w2)
label_wave2 = f"$\\Psi$ ($A={A2}$, $k={k2}$, $\\omega={w2}$)"

A3, k3, w3 = 0.25, 2, 3
y_data_wave3 = hf.func_ab_to_grid(travelling_wave, x_array, t_array, amplitude = A3, wavenumber = k3, omega = w3)
label_wave3 = f"$\\Psi$ ($A={A3}$, $k={k3}$, $\\omega={w3}$)"

# generate canvas
canvas = SingleCanvas(
    figsize=(4,4), 
    dpi=400, 
    time_array=t_array, 
    axis_limits=[0,2*np.pi,-1,1], 
    axis_labels=['$x$','$y$']
    )

# generate waves
wave1 = AnimatedLine(label_wave1, x_data, y_data_wave1)
wave1.set_styling_properties(color = 'tab:blue')

wave2 = AnimatedLine(label_wave2, x_data, y_data_wave2)
wave2.set_styling_properties(color = 'tab:orange')

wave3 = AnimatedLine(label_wave3, x_data, y_data_wave3)
wave3.set_styling_properties(color = 'tab:red')

canvas.add_artist(wave1, in_legend = True)
canvas.add_artist(wave2, in_legend = True)
canvas.add_artist(wave3, in_legend = True)

# construct legend
canvas.construct_legend(loc = 'upper right', fontsize = 'x-small')

# render animation
sines_animation = Animation(canvas)
sines_animation.render('examples/travelling_waves/travelling_waves.mp4')          
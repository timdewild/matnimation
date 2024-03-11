import sys
import os

# we add the ~/matnimation directory to be able to import the 'src' module
sys.path.append(os.path.abspath(''))              

import matplotlib.colors as colors
import numpy as np
from src.matnimation.animation.animation import Animation
from src.matnimation.artist.animated.animated_single_scatter import AnimatedSingleScatter
from src.matnimation.artist.static.static_line import StaticLine
from src.matnimation.canvas.single_canvas import SingleCanvas
from src.matnimation.artist.animated.animated_text import AnimatedText, AnimatedTextBbox

# generate animation of particle moving in (x,y) space according to:
# x(t) = t
# y(t) = sin(t) 
# over time interval t = [0,2pi]

#--- Generate Data ---#

# generate timearray
tmin, tmax, N_timesteps = 0, 2*np.pi, 60
time_array = np.linspace(tmin, tmax, N_timesteps)

# strings for time label
timelabel_str_data = ['$t={time:.{digits}f}$ '.format(time=t, digits=2) for t in time_array]

# generate particle's position at all timesteps
x_particle = time_array
y_particle = np.sin(time_array)

# generate trajectory
x_trajectory = np.linspace(0, 2*np.pi, 100)
y_trajectory = np.sin(x_trajectory)


#--- Construct Canvas ---#
canvas = SingleCanvas(
    figsize=(4,4),
    dpi=400,
    time_array=time_array,
    axis_limits=[0, 2*np.pi, -1, 1], 
    axis_labels=['$x$', '$y$'],
)

#--- Trajectory ---#

# instantiate trajectory
trajectory = StaticLine(
    name = 'Trajectory', 
    x_data = x_trajectory, 
    y_data = y_trajectory
    )

# set styling properties
trajectory.set_styling_properties(
    linewidth = 0.5, 
    linestyle = 'dotted', 
    color = 'k')

# add trajectory to canvas
canvas.add_artist(trajectory, in_legend = True)

#--- Particle ---#

# instantiate particle
particle = AnimatedSingleScatter(
    name = 'Particle', 
    x_data = x_particle, 
    y_data = y_particle)

# set styling properties
particle.set_styling_properties(
    markeredgecolor = 'tab:blue', 
    markerfacecolor = colors.to_rgba('tab:blue', 0.4)
    )

# add particle to canvas
canvas.add_artist(particle, in_legend = True)

#--- Construct Legend ---#
canvas.construct_legend(
    fontsize = 'x-small', 
    ncols = 2, 
    loc = 'lower center'
    )

#--- Render Animation ---#
animation = Animation(canvas, interval = 15)
animation.render('examples/oscillating_particle/oscillating_particle.mp4')
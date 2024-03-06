import sys
import os

#we add the ~/matnimation directory to be able to import the 'src' module
sys.path.append(os.path.abspath(''))              

import matplotlib.colors as colors
import numpy as np
from src.matnimation.animation.animation import Animation
from src.matnimation.artist.animated.animated_single_scatter import AnimatedSingleScatter
from src.matnimation.artist.static.static_line import StaticLine
from src.matnimation.canvas.single_canvas import SingleCanvas

# generate animation of particle moving in (x,y) space according to:
# x(t) = t
# y(t) = sin(t) 
# over time interval t = [0,2pi]

# generate animation data

time_array = np.linspace(0, 2*np.pi, 60)
x_particle = time_array
y_particle = np.sin(time_array)

# generate canvas
canvas_particle = SingleCanvas(
    figsize=(4,4),
    dpi=400,
    time_array=time_array,
    axis_limits=[0, 2*np.pi, -1, 1],
    axis_labels=['$x$', '$y$'],
)

# add static trajectory
trajectory = StaticLine('Trajectory', x_particle, y_particle)
trajectory.set_styling_properties(linewidth = 0.5, linestyle = 'dotted', color = 'k')
canvas_particle.add_artist(trajectory, in_legend = True)

# add animated single scatter artist to represent particle
particle = AnimatedSingleScatter('Particle', x_particle, y_particle)
particle.set_styling_properties(markeredgecolor = 'tab:blue', markerfacecolor = colors.to_rgba('tab:blue', 0.4))
canvas_particle.add_artist(particle, in_legend = True)

canvas_particle.construct_legend(fontsize = 'x-small', ncols = 2, loc = 'lower center')

# generate and render animation
particle_animation = Animation(canvas_particle, interval = 15)
particle_animation.render('examples/oscillating_particle/oscillating_particle2.mp4')
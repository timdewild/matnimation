import matplotlib.colors as colors
import numpy as np
from src.matnimation.animation.animation import Animation
from src.matnimation.artist.animated.animated_single_scatter import AnimatedSingleScatter
from src.matnimation.artist.static.static_line import StaticLine
from src.matnimation.canvas.single_canvas import SingleCanvas

# generate animation of particle moving in (x,y) space according to:
# x(t) = t
# y(t) = sin(t) 
# over time t = [0,2pi]

# generate animation data

time_array = np.linspace(0, 2*np.pi, 60)
x_particle = time_array
y_particle = np.sin(time_array)

# generate canvas
canvas_particle = SingleCanvas(
    (4,4),
    400,
    time_array,
    [0, 2*np.pi, -1, 1],
    ['$x$', '$y$'],
)

# add static trajectory
trajectory = StaticLine('Trajectory', x_particle, y_particle)
trajectory.set_styling_properties(linewidth = 0.5, linestyle = 'dotted', color = 'k')
canvas_particle.add_artist(trajectory, in_legend = True)

# add animated single scatter artist to represent particle
particle = AnimatedSingleScatter('Particle', x_particle, y_particle)
particle.set_styling_properties(markeredgecolor = 'tab:blue', markerfacecolor = colors.to_rgba('tab:blue', 0.4))
canvas_particle.add_artist(particle, in_legend = True)

legend_styling = dict(fontsize = 'x-small', ncols = 2, loc = 'upper center', framealpha = 1)

canvas_particle.construct_legend()

# generate and render animation
particle_animation = Animation(canvas_particle, interval = 15)
particle_animation.render('examples/oscillating_particle.mp4')
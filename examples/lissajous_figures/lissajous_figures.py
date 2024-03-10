import sys
import os

# we add the ~/matnimation directory to be able to import the 'src' module
sys.path.append(os.path.abspath(''))              

import matplotlib.colors as colors
import numpy as np
from src.matnimation.animation.animation import Animation
from src.matnimation.artist.animated.animated_single_scatter import AnimatedSingleScatter
from src.matnimation.artist.static.static_line import StaticLine
from src.matnimation.canvas.multi_canvas import MultiCanvas
from src.matnimation.artist.animated.animated_text import AnimatedText, AnimatedTextBbox

#--- Generate Data ---#

# generate timearray
tmin, tmax, N_timesteps = 0, 2*np.pi, 200
time_array = np.linspace(tmin, tmax, N_timesteps)

# strings for time label
timelabel_str_data = ['$\theta={time:.{digits}f}$'.format(time=t, digits=2) for t in np.linspace(0,10,N_timesteps)]

#--- Generate MultiCanvas of 1 x 3 plots ---#
canvas = MultiCanvas(
    figsize = (9,3.5),
    dpi = 400,
    time_array = time_array,
    nrows = 1,
    ncols = 3,
    axes_limits = [[-2,2,-2,2]]*3,
    axes_labels = [['$x$', '$y$'],['$x$', ''],['$x$', '']],
)

# set aspect ratio to equal and visually appealing xticks and yticks manually
for col in range(3):
    canvas.set_axis_properties(
        row = 0, 
        col = col, 
        aspect = 'equal', 
        xticks = np.linspace(-2,2,5), 
        yticks = np.linspace(-2,2,5)
        )


#--- Generate Lissajous Curves ---#

def lissajous_curve(t, a = 1, b = 1, delta = 0, A = 1, B = 1):
    x = A * np.sin(a * t + delta)
    y = B * np.sin(b * t)

    return x, y

# Curves for subplot 0, 1, 2
curve0_data = lissajous_curve(time_array, a = 1, b = 2, delta = np.pi/2)
curve1_data = lissajous_curve(time_array, a = 3, b = 2, delta = np.pi/2)
curve2_data = lissajous_curve(time_array, a = 3, b = 4, delta = np.pi/2)

# Parametric curves
curve0 = StaticLine(
    name = 'Curve 0',
    x_data = curve0_data[0],
    y_data = curve0_data[1]
)

curve0.set_styling_properties(lw = 1)

curve1 = StaticLine(
    name = 'Curve 1',
    x_data = curve1_data[0],
    y_data = curve1_data[1]
)

curve1.set_styling_properties(lw = 1, color = 'tab:red')

curve2 = StaticLine(
    name = 'Curve 2',
    x_data = curve2_data[0],
    y_data = curve2_data[1]
)

curve2.set_styling_properties(lw = 1, color = 'tab:green')

canvas.add_artist(curve0, row = 0, col = 0)
canvas.add_artist(curve1, row = 0, col = 1)
canvas.add_artist(curve2, row = 0, col = 2)

# Trajectory dots
dot0 = AnimatedSingleScatter(
    name = 'Dot 0',
    x_data = curve0_data[0],
    y_data = curve0_data[1]
)

dot1 = AnimatedSingleScatter(
    name = 'Dot 1',
    x_data = curve1_data[0],
    y_data = curve1_data[1]
)

dot2 = AnimatedSingleScatter(
    name = 'Dot 2',
    x_data = curve2_data[0],
    y_data = curve2_data[1]
)

canvas.add_artist(dot0, row = 0, col = 0)
canvas.add_artist(dot1, row = 0, col = 1)
canvas.add_artist(dot2, row = 0, col = 2)

dot0.set_styling_properties(markeredgecolor = 'tab:blue', markerfacecolor = colors.to_rgba('tab:blue',0.5), markeredgewidth = 0.5)
dot1.set_styling_properties(markeredgecolor = 'tab:red', markerfacecolor = colors.to_rgba('tab:red',0.5), markeredgewidth = 0.5)
dot2.set_styling_properties(markeredgecolor = 'tab:green', markerfacecolor = colors.to_rgba('tab:green',0.5), markeredgewidth = 0.5)

fig = canvas.get_figure()
fig.savefig('examples/lissajous_figures/canvas_3x1.jpg', dpi = 400)

#--- Render Animation ---#
animation = Animation(canvas, interval = 10)
animation.render('examples/lissajous_figures/lissajous_figures.mp4')




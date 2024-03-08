# Tutorial: Oscillating Particle Animation
In this tutorial, we show how to use `matnimation` to make a simple animation of a particle moving along an oscillating trajectory. This trajectory is given by the parametric equations:
```math
\begin{align*}
x(t) &= t \\
y(t) &= \sin t
\end{align*}
```
for $t\in [0,2\pi]$. See the final animation below. We will go through the code ([oscillating_particle.py](/examples/oscillating_particle/oscillating_particle.py)) for this animation step by step. 

https://github.com/timdewild/matnimation/assets/93600756/d51b1a3f-6b0b-476b-8277-93d33d578183

## General Workflow
We start by describing the general workflow to make animations. The animations are build using three base classes/objects: 
* `Canvas`

    The canvas object should be thought of as the stage on which the animations take place. The canvas defines the figure with (possibly multiple) axes on which `BaseArtist` objects live. 

    > **Note** The `Canvas` class has multiple subclasses such as `SingleCanvas` for a single pair of axes or `MultiCanvas` for multiple pairs of axes.   

* `BaseArtist`

    An artist that lives on the canvas. Examples are e.g. a line, circle, vector field or image, but also a textbox is considered an artist. Artists can be _static_ or _animated_, as implemented via the `StaticArtist` and `AnimatedArtist` subclasses. As the name suggests, static artists do not change during the animation. Animated artists change in some way or another during the animation. 

    > **Example** A line can change its shape during the animation, just as the text string in a textbox can change over time. 

* `Animation`

    The canvas and (collection of) artists are rendered into an actual animation (video) using the `Animation` class. This class runs Matplotlib's `animation.FuncAnimation` under it's hood ([docs](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation)).  

## Step-by-Step Process
Now we will go through the code in the file [oscillating_particle.py](/examples/oscillating_particle/oscillating_particle.py) step by step to demonstrate how the above animation is made.

### Step 0: Import Dependencies
We first import the required modules. For local modules, such as `matnimation`, python will search in the current file's directory by default, which is `~/matnimation/examples/oscillating_particle` in our case. However, the source code is located in `~/matnimation/src`. Therefore, we add the root directory `~/matnimation` to the `sys.path` list, allowing the interpreter to find the source code of the module. 

```python
import sys
import os

# we add the ~/matnimation directory to be able to import the 'src' module
sys.path.append(os.path.abspath(''))
```

Then we can import all the required dependencies.

```python
import matplotlib.colors as colors
import numpy as np

from src.matnimation.animation.animation import Animation
from src.matnimation.artist.animated.animated_single_scatter import AnimatedSingleScatter
from src.matnimation.artist.static.static_line import StaticLine
from src.matnimation.canvas.single_canvas import SingleCanvas
```

### Step 1: Generate Data
We start by descritizing time and store all timesteps in `time_array`.

```python
# generate timearray
tmin, tmax, N_timesteps = 0, 2*np.pi, 60
time_array = np.linspace(tmin, tmax, N_timesteps)
```

> [!NOTE]
> In `time_array`, we chose the number of timesteps `N_timesteps` to be 60, which means that the final animation will contain 60 frames in total. At a later stage, when we construct the `Animation` object, we will set the time `interval` between each frame. The total duration of the rendered animation will then be `N_timesteps * interval`. 

In the animation, the particle moves in the ($x,y$) plane according to the parametric equations. Hence, the next step is to find the coordinates of the particle along its trajectory at all timesteps.

```python
# generate particle's position at all timesteps
x_particle = time_array
y_particle = np.sin(time_array)
```

Finally, we wish to find the trajectory, which is simply given by $y=\sin x$. 

```python
# generate trajectory
x_trajectory = np.linspace(0, 2*np.pi, 100)
y_trajectory = np.sin(x_trajectory)
```

### Step 2: Construct Canvas
Now we generate a `canvas` that will host the all artists in the animation (i.e. the particle and trajectory), which will be contructed in the next step. We make a simple animation with only a single panel, so we use `SingleCanvas`. We set the `figsize` in inches, the resolution `dpi` in dots-per-inch, the `time_array`, the `axis_limits` and the `axis_labels`. 

```python
canvas = SingleCanvas(
    figsize = (4,4),
    dpi = 400,
    time_array = time_array,
    axis_limits = [0, 2*np.pi, -1, 1],
    axis_labels = ['$x$', '$y$']
)
```

> [!IMPORTANT]
> The canvas should be thought of as the stage on which animated (and static) objects live over time. Therefore, it takes the `time_array` as argument. 

### Step 3: Construct Artists
Now we are in the position to contruct the artists living on the canvas. In our case we have two: the particle and its trajectory. Naturally, the trajectory is a static line represented by `StaticLine`, and the particle is depicted as a moving dot, represented by `AnimatedSingleScatter`. 

> [!NOTE]
> `StaticLine` and `AnimatedSingleScatter` are subclasses of `StaticArtist` and `AnimatedArtist`, respectively. 

The construction of an artist consists of three steps:
1. Instantiating the artist.
2. Setting styling properties of the artist.
3. Adding the artist to the canvas.

#### Trajectory
First we construct the trajectory by providing the name `'Trajectory'` and the trajectory data to `StaticLine`.

```python
# instantiate trajectory
trajectory = StaticLine(
    name = 'Trajectory', 
    x_data = x_trajectory, 
    y_data = y_trajectory
    )
```
Then we set the styling properties.  

```python
# set styling properties
trajectory.set_styling_properties(
    linewidth = 0.5, 
    linestyle = 'dotted', 
    color = 'k'
    )
```

Under its hood, `StaticLine` uses Matplotlib's `Line2D` class. When setting styling properties via `set_styling_properties`, all keywords that are allowed in the `set` method of `Line2D` can be passed ([docs](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html)). 

> [!NOTE]
> Practically all artists in `matnimation` are based on some form of a Matplotlib `Artist`. To find which keywords may be passed to the `set_styling_properties` method, look at the documentation on the `set` method of the corresponding Matplotlib `Artist`. 

Finally we add the `trajectory` to the `canvas` via the `add_artist` method and specify that it should be included in the canvas' legend via `in_legend = True`.

```python
# add trajectory to canvas
canvas.add_artist(trajectory, in_legend = True)
```

> [!IMPORTANT]
> For the legend to be *visible* on the canvas, it should still be constructed using the `construct_legend()` method of the `canvas` object, even if artists are already added to the legend via the `in_legend` keyword. The legend label will be the `name` of the artist, in this case `'trajectory'`. 

#### Particle
Now we repeat the same process for the particle, with the difference that we now use an instance of `AnimatedSingleScatter`.

```python
# instantiate particle
particle = AnimatedSingleScatter(
    name = 'Particle', 
    x_data = x_particle, 
    y_data = y_particle
    )

# set styling properties
particle.set_styling_properties(
    markeredgecolor = 'tab:blue', 
    markerfacecolor = colors.to_rgba('tab:blue', 0.4)
    )

# add particle to canvas
canvas.add_artist(particle, in_legend = True)
```

We provided the animation data (the $x$ and $y$ coordinates at each timestep) via the arrays `x_particle` and `y_particle`. 

> [!IMPORTANT]
> For all instances of `AnimatedObject` used in an animation, the dimensions of the animation data must be compatible with `time_array`. In our case this means that the length of `x_particle` and `y_particle` must equal that of `time_array`. This makes sense: we need the coordinates of the particle at each timestep. 

### Step 5: Add a Legend
Next we add a legend to the `canvas` via the `construct_legend()` method. This method accepts keyword arguments `**legend_styling` for legend styling. You can pass all kwargs listed under 'Other Parameters' in the Matplotlib [docs](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend) of `Axes.legend`. We have set the fontsize to extra small and the location to lower center. 

```python
canvas.construct_legend(
    fontsize = 'x-small', 
    ncols = 2, 
    loc = 'lower center'
    )
```

### Step 6: Construct and Render Animation
Lastly, we construct an `Animation` object which takes the `canvas` as input, in addition to the `interval` keyword which specifies the time interval between succesive frames in milliseconds (ms). The default is set to 30 ms. We render the animation via the `render` method, which takes the filename (or filepath) as input. The final animation will have a duration of `N_timesteps * interval` milliseconds.

```python
animation = Animation(canvas, interval = 15)
animation.render('examples/oscillating_particle/oscillating_particle.mp4')
```


















 
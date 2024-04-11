# matnimation

A wrapper to quickly make Matplotlib animations. 

- [Installation](#installation)
    - [Option 1: Cloning Repository](#option-1-cloning-repository)
    - [Option 2: Git Submodules](#option-2-git-submodules)
    - [Importing the Modules](#importing-the-modules)
- [Methodology and Usage](#methodology-and-usage)
    - [Three Building Blocks](#three-building-blocks)
    - [Example Workflow](#example-workflow)
    - [Advantages of `matnimation`](#advantages-of-matnimation)
- [Tutorials & Examples](#tutorials-and-examples)

# Installation
`matnimation` is not an official python package that can be installed locally. Instead, you have two options to use `matnimation` yourself. 

### Option 1: Cloning Repository
The first, and simplest way, is to clone its Github repository inside your project folder. Suppose your project folder is called `my_animation_project`, open your terminal and change directory to that folder. Then use:
```python
git clone git@github.com:timdewild/matnimation.git
``` 
for SSH-cloning using or 
```python
git clone https://github.com/timdewild/matnimation.git
```
for https-cloning. In case new features are added to `matnimation` and you want to use them, you have to clone again. 

### Option 2: Git Submodules
A more versatile way of using `matnimation` in your animation project is to add it as a submodule to your project's repository. For this to work your folder `my_animation_project` must be a git repository. To add `matnimation` as a submodule, use the command:
```python
git add submodule https://github.com/timdewild/matnimation.git
```
This will only stage the submodule, you still need to commit the submodule:
```python
git commit -m "Added the submodule to the project."
git push
```
A submodule always refers to a specific commit, so if you commit changes to `matnimation`, those are not automatically implemented in the submodule. To update the submodule to refer to the newest commit, you run:
```python
git submodule update
```
For more details on git submodules, see the [documentation](https://git-scm.com/book/en/v2/Git-Tools-Submodules).

### Importing the Modules
For both options, there should now be a subfolder in `my_animation_project` called `matnimation` that contains (a version of) its source code. Let `animation.py` be the file in which you build the animation. The structure of your project then looks like:
```
my_animation_project
└── matnination
└── animation.py
```
Now, we wish to import the modules in `matnimation` in our `animation.py` file. To do so, we have to tell python where to look for these modules: inside the `matnimation` folder. We do this by adding the path to the `matnimation` folder at the top of the file:

```python
# file: animation.py

import sys
import os

sys.path.append(os.path.abspath('matnimation'))
```

This is the simplest setup, if your project contains multiple subfolders with `.py` files that import `matnimation`, the correct paths should be included in each of these files. For an example of how this works, see e.g. [this](https://github.com/timdewild/fourier-series-epicycles) repo. 

# Methodology and Usage
Before we give a detailed example of how you can use `matnimation` to easily make Matplotlib animations, we will first give an overview of its working principle and main building principle. After that, we will give an example and explicitly compare `matnimation`'s workflow to how the same animation would be constructed in the conventional way (as described in Matplotlib's [documentation](https://matplotlib.org/stable/users/explain/animations/animations.html)).

## Three Building Blocks
The working principle of `matnimation` revolves around three fundamental objects/classes:
* `Canvas`

    The canvas object should be thought of as the stage on which the animations take place. The canvas defines the figure with (possibly multiple) axes on which `BaseArtist` objects live. 

    > **Note** The `Canvas` class has multiple subclasses such as `SingleCanvas` for a single pair of axes or `MultiCanvas` for multiple pairs of axes.   

* `BaseArtist`

    An artist that lives on the canvas. Examples are e.g. a line, circle, vector field or image, but also a textbox is considered an artist. Artists can be _static_ or _animated_, as implemented via the `StaticArtist` and `AnimatedArtist` subclasses. As the name suggests, static artists do not change during the animation. Animated artists change in some way or another during the animation. 

    > **Example** A line can change its shape during the animation, just as the text string in a textbox can change over time. 

* `Animation`

    The canvas and (collection of) artists are rendered into an actual animation (video) using the `Animation` class. This class runs Matplotlib's `animation.FuncAnimation` under it's hood ([docs](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation)). 

## Example Workflow
Now we are in the position to describe how a simple animation would be constructed using `matnimation` in four steps. More complex animations will still follow the same steps. In this example, shown below, we animate a particle that follows the following parametric trajectory:
```math
\begin{equation}
    x(t) = \frac{1}{2}t \sin(t),\quad\quad y(t) = \frac{1}{2}t \cos(t)
\end{equation}
```
where we take the wavenumber we take the time paramter to be in the range $t\in[0,4\pi]$. We want to (a) show the particle at every moment in time and (b) add a trace (line) of the completed part of the trajectory so far. We will animate them using the `AnimatedSingleScatter` and `AnimatedTrace` artists, respectively. 

https://github.com/timdewild/matnimation/assets/93600756/50f7ada2-e2df-4224-ab1e-6d708f25f6c0

### Step 0: Import Dependencies
We start by importing all the dependencies.
```python
import numpy as np
import sys
import os

# to be able to find ~/matnimation directory
sys.path.append(os.path.abspath('matnimation'))

from matnimation.src.matnimation.animation.animation import Animation
from matnimation.src.matnimation.canvas.single_canvas import SingleCanvas
from matnimation.src.matnimation.artist.animated.animated_single_scatter import AnimatedSingleScatter
from matnimation.src.matnimation.artist.animated.animated_trace import AnimatedTrace
```

### Step 1: Generating Data
We discretize the temporal interval into 200 timesteps in `t_array`. For all these timesteps, we compute the trajectory of the particle via the function `trajectory(t)`. 
```python
N_time_steps = 200
t_array = np.linspace(0, 4*np.pi, N_time_steps)

def trajectory(t):
    return 0.5 * t * np.sin(t), 0.5 * t * np.cos(t)

x_trajectory, y_trajectory = trajectory(t_array)
```
The animation should be thought of as a collection of frames, one for each time value in `t_array`, meaning we have a total of 200 frames in this animation. As mentioned, we represent the particle as a moving dot using the `AnimatedSingleScatter` artist and the trace using the `AnimatedTrace`. The data (`x_data` and `y_data` parameters) that must be provided to these artists are the same. 

> [!NOTE]
> The format in which data must be provided to artists differs: see the docstring of the artist in question to find out how data must be provided. 

### Step 2: Define Canvas
Next, we constuct a canvas on which the artists, to be constructed in the next step, live. We make a simple animation with only a single panel, so we use `SingleCanvas`. We set the `figsize` in inches, the resolution `dpi` in dots-per-inch, the `time_array`, the `axis_limits` and the `axis_labels`. Simple mathmetical expressions are passed into the labels via the double dollar syntax `$$`. 

```python
canvas = SingleCanvas(
    figsize = (4, 5),
    dpi = 400,
    time_array = t_array,
    axis_limits = [-2*np.pi, 2*np.pi, -2*np.pi, 2*np.pi],
    axis_labels = ['$x$', '$y$']
)

canvas.set_axis_properties(aspect = 'equal')
```
In the last line, we have set the aspect ratio of the axes to `'equal'`, so that it is visualized in the correct proportion.

> [!IMPORTANT]
> The canvas should be thought of as the stage on which animated (and static) objects live over time. Therefore, it takes the `time_array` as argument. The dynamic behavior of all animated artists should be defined for all timesteps in `t_array`. 

### Step 3: Construct Artists
Now we are in the position to construct the artists: the particle and trace. 

```python
particle = AnimatedSingleScatter(
    name = 'Particle',
    x_data = x_trajectory,
    y_data = y_trajectory,
)

trajectory_trace = AnimatedTrace(
    name = 'Trajectory Trace',
    x_data = x_trajectory,
    y_data = y_trajectory
)
```

After construction, we add the artists to the canvas via:

```python
canvas.add_artist(particle)
canvas.add_artist(trajectory_trace)
```

In this example we only added tow artists to the canvas, but note that in this way you can systematically add as many artists to the canvas as you like. 

### Step 4: Construct and Render Animation
Lastly, we construct an `Animation` object which takes the `canvas` as input, in addition to the `interval` keyword which specifies the time interval between succesive frames in milliseconds (ms). The default is set to 30 ms. We render the animation via the `render` method, which takes the filename (or filepath) as input. The final animation will have a duration of `N * interval` milliseconds. In our case, we have `N_timesteps=200` steps or frames and take the interval to be 20 ms, so that our final animation is 4 seconds. 

```python
animation = Animation(canvas, interval = 20)
animation.render('parametric_particle_using_matnimation.mp4')
```

# Advantages of `matnimation`
Below, we show the full workflow of the example above and compare it to the conventional approach in which animations are made using Matplotlib, as described in the [docs](https://matplotlib.org/stable/users/explain/animations/animations.html).

## The `matnimation` Approach
The complete contents of the file `animation.py` are shown below, highlighting the four sequential steps required to construct the animation. 

```python

# Step 0: Import Dependencies 
import numpy as np
import sys
import os

# to be able to find ~/matnimation directory
sys.path.append(os.path.abspath('matnimation'))

from matnimation.src.matnimation.animation.animation import Animation
from matnimation.src.matnimation.canvas.single_canvas import SingleCanvas
from matnimation.src.matnimation.artist.animated.animated_single_scatter import AnimatedSingleScatter
from matnimation.src.matnimation.artist.animated.animated_trace import AnimatedTrace

# Step 1: Generating Data
N_time_steps = 200
t_array = np.linspace(0, 4*np.pi, N_time_steps)

def trajectory(t):
    return 0.5 * t * np.sin(t), 0.5 * t * np.cos(t)

x_trajectory, y_trajectory = trajectory(t_array)

# Step 2: Define Canvas
canvas = SingleCanvas(
    figsize = (4, 5),
    dpi = 400,
    time_array = t_array,
    axis_limits = [-2*np.pi, 2*np.pi, -2*np.pi, 2*np.pi],
    axis_labels = ['$x$', '$y$']
)

canvas.set_axis_properties(aspect = 'equal')

# Step 3: Construct Artists
particle = AnimatedSingleScatter(
    name = 'Particle',
    x_data = x_trajectory,
    y_data = y_trajectory,
)

trajectory_trace = AnimatedTrace(
    name = 'Trajectory Trace',
    x_data = x_trajectory,
    y_data = y_trajectory
)

canvas.add_artist(particle)
canvas.add_artist(trajectory_trace)

# Step 4: Construct and Render Animation
animation = Animation(canvas, interval = 20)
animation.render('parametric_particle_using_matnimation.mp4')
```

## The `matplotlib` Approach
Now we show how you can make the exact same animation, using the conventional approach as described in Matplotlib's [animation documentation](https://matplotlib.org/stable/users/explain/animations/animations.html). The basic idea is to generate a `Figure` object, add `Artist` objects to this figure instance and write an `animate()` function that encodes how the artists change from frame to frame. Both the figure instance and `animate()` are then passed to `FuncAnimation`, which returns the animation object that can be saved as a video file. 

```python
from matplotlib import pyplot as plt 
import numpy as np 
from matplotlib.animation import FuncAnimation 

# initializing a figure and axis
fig, axis = plt.subplots() 
fig.set_size_inches(4,5)

# marking the x-axis and y-axis 
axis.set_xlim(-2 * np.pi, 2 * np.pi)
axis.set_ylim(-2 * np.pi, 2 * np.pi)

# set aspect ratio
axis.set_aspect('equal')

# update grid and bkg facecolor
axis.grid(
	True, 
	color=u'white', 
	lw=1.5, 
	zorder=0
	)
axis.set_facecolor('#EEEEEE')

# set x and y labels
axis.set_xlabel('$x$')
axis.set_ylabel('$y$')

# initializing dot and trace 
particle = axis.scatter([], [], zorder = 3) 
trace, = axis.plot([], [])

N_time_steps = 200
t = np.linspace(0, 4*np.pi, N_time_steps)

x_trajectory = 0.5 * t * np.sin(t)
y_trajectory = 0.5 * t * np.cos(t)

def animate(i):   
    particle.set_offsets(np.column_stack([x_trajectory[i], y_trajectory[i]])) 
    trace.set_data(x_trajectory[:i+1], y_trajectory[:i+1])
	
    return particle, trace,

anim = FuncAnimation(
    fig, animate,  
    frames = len(t), 
    interval = 20, 
	) 

anim.save('parametric_particle_using_FuncAnimation.mp4')
```

## Comparing the Two Approaches
We note a number of differences in the approaches above:

- **Scalability** - In the Matplotlib approach, animated artists are constructed in a two-step process. First they are initialized and added to the figure. Only after that, in the animation function `animate()`, their dynamic behavior is specified (i.e. how they change from frame to frame). For multiple animated artists, the function quickly becomes extensive and difficult to read. In `matnimation`, the dynamic behavior of the artists is defined when they are instantiated. Under the hood of `matnimation`'s `Animation` class, the animation function is created automatically. Therefore, multiple artists can be added in systematic and clear way, increasing scalability.

- **Consistency** - There is another, more practical reason, why automatic creation of the animation function is advantageous. In Matplotlib's animation function, the dynamic behavior of artists is defined via `set_` methods. However, the naming of these methods is not consistent from artist to artist. Take the example above: for the `particle`, the method is called `set_offsets()` and for the `trace` it is called `set_data()`. Furthermore, the method signatures are not consistent as `set_offsets()` takes one 2D array as input, while `set_data()` takes two 1D arrays as arguments. By creating the animation function automatically under the hood of `Animation`, the user does not have to deal with the naming and signature inconsistencies of the `set_` methods.

- **Cohesion** - Although not immediately appararent from the example above, in practice it often happens for more complex animations that the animation function deals with both _generating_ the data (e.g. calculating the new position of a particle) and _updating_ the artist with this data (see e.g. [this](https://matplotlib.org/stable/gallery/animation/double_pendulum.html) example). However, strictly speaking the function should be only concerned with updating the animated artist from frame to frame and not with the generation of the data that is used to do this. In `matnimation`, all data of an animated artist is calculated beforehand and then fed to the `AnimatedArtist`. That is, the two tasks are clearly separated, leading to more cohesion.

- **Static vs Animated Artists** - In Matplotlib's approach, there is no clear distinction between static and animated artists. More specifically, to find out whether an artist is animated or not, one should check if the artist is updated in the animation function or not. However, already from the creation of a static artist, it should be clear that it does not change during the animation. In `matnimation`, this distinction between an `AnimatedArtist` and `StaticArtist` is made very apparent already in terms of naming. 

# Tutorials and Examples
Tutorials and examples are given in the folder `examples`. They are also listed in [this](./examples/examples.md) overview. 

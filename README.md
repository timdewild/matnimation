# matnimation

A wrapper to quickly make Matplotlib animations. 

> [!WARNING]
> This README file is not complete yet, but will be updated soon! Take a sneak peak at the [examples](./examples/examples.md)!

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

https://github.com/timdewild/matnimation/assets/93600756/6388ec0b-f749-44fc-9153-2bec5a076cb2

## Example Workflow
Now we are in the position to describe how a simple animation would be constructed using `matnimation` in four steps. More complex animations will still follow the same steps. In this example, shown above, we animate a travelling sine wave, described by:
```math
\begin{equation}
    y(x,t) = \sin (kx-\omega t),
\end{equation}
```
where we take the wavenumber $k=2\pi$ and radial frequency $\omega = 4\pi$.

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
from matnimation.src.matnimation.artist.animated.animated_line import AnimatedLine
from matnimation.src.matnimation.helper.helper_functions import HelperFunctions
```

### Step 1: Generating Data
We have to set the spatial and temporal boundaries of our animation, we take $x\in[0,4]$ and $t\in[0,1]$. Those intervals are descretized by the arrays:
```python
N, M = 1000, 100
x_array = np.linspace(0,4,M)
t_array = np.linspace(0,1,N)
```
The animation should be thought of as a collection of frames, one for each time value in `t_array`, meaning we have a total of 100 frames in this animation. Then we define a function that describes the travelling sine wave:
```python
def wave(x,t):
    """Returns the traveling waveform y(x,t) = sin(kx - wt) with k = 2pi and w = 4pi."""

    y = np.sin(2 * np.pi * (x - 2*t)) 

    return y
```
We will animate the travelling sine wave using the `AnimatedLine` artist, which requires the $y$ coordinates of the line at all timesteps in the animation. That is, we have to find the waveform $y(x,t)$ for all $x$ in `x_array` at all timesteps $t$ in `t_array`. The data must be passed into `AnimatedLine` as a 2D numpy array of shape `(M, N)`, which we will call `ydata`. 
```math
\begin{equation}
    \boldsymbol{A}=\left( 
    \begin{array}{c|c|c}
    \Psi(x_0, t_0) & \cdots & \Psi(x_0, t_N) \\
    \vdots &  & \vdots \\
    \Psi(x_M, t_0) & \cdots & \Psi(x_M, t_N)
    \end{array} 
    \right)
\end{equation}
```

This means that `ydata[:,i]` gives the full wavefrom $y(x,t_i)$ at the $i$-th timestep. We use `func_ab_to_grid` from the `HelperFunctions` class to generate the data.

```python
ydata = HelperFunctions.func_ab_to_grid(
    func = wave,
    a = x_array,
    b = t_array
    )
```

> [!NOTE]
> Given a mathematical function of two parameters $f(a,b)$ called `func(a,b)` and two arrays `a_array` and `b_array`, `func_ab_to_grid` returns a 2D array with entry `[i,j]` corresponding to `func(a_array[i], b_array[j])`.

### Step 2: Define Canvas
Next, we constuct a canvas on which the artists, to be constructed in the next step, live. We make a simple animation with only a single panel, so we use `SingleCanvas`. We set the `figsize` in inches, the resolution `dpi` in dots-per-inch, the `time_array`, the `axis_limits` and the `axis_labels`. Simple mathmetical expressions are passed into the labels via the double dollar syntax `$$`. 

```python
canvas = SingleCanvas(
    figsize = (4,4),
    dpi = 400,
    time_array = t_array,
    axis_limits = [0, 4, -2, 2],
    axis_labels = ['$x$', '$y(x,t)$']
)
```

> [!IMPORTANT]
> The canvas should be thought of as the stage on which animated (and static) objects live over time. Therefore, it takes the `time_array` as argument. The dynamic behavior of all animated artists should be defined for all timesteps in `t_array`. 

### Step 3: Construct Artists
Now we are in the position to construct the artists. In our example we only have one artist, the `AnimatedLine` representing the travelling wave. 

```python
travelling_wave = AnimatedLine(
    name = 'Travelling Wave',
    x_data = x_array,
    y_data = ydata,
)
```

We provide a `name`, the `x_data` which is simply `x_array` and pass the waveform at all timesteps via `ydata`. In this case, only the $y$ coordinates of the animated line change over time and the $x$ coordinates are fixed. This need not be the case, if the latter also change you can pass a 2D array to `x_data` of the same format as `ydata`. Now we add `travelling_wave` to the canvas via:

```python
canvas.add_artist(travelling_wave)
```

In this example we only added one artist to the canvas, but note that in this way you can systematically add as many artists to the canvas as you like. 

### Step 4: Construct and Render Animation
Lastly, we construct an `Animation` object which takes the `canvas` as input, in addition to the `interval` keyword which specifies the time interval between succesive frames in milliseconds (ms). The default is set to 30 ms. We render the animation via the `render` method, which takes the filename (or filepath) as input. The final animation will have a duration of `N_timesteps * interval` milliseconds. In our case, 100 timesteps or frames and take the interval to be 20 ms, so that our final animation is 2 seconds. 

```python
animation = Animation(canvas, interval = 20)
animation.render('sine_wave_using_matnimation.mp4')
```














 


























# Examples
Examples are given in the folder `examples`. They are also listed in [this](./examples/examples.md) overview. 
